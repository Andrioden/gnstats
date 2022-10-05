from typing import List, Optional, Union

from fastapi import APIRouter, HTTPException

from api.decorators import ensure_db_context
from api.utils import current_user_person_name
from models.api.game_night import GameNightCreate, GameNightUpdate
from models.api.vote import VoteCreate, VoteUpdate
from models.db.game_night import GameNight
from models.db.person import Person
from models.db.vote import Vote
from repos.game_night import GameNightRepo
from repos.vote import VoteRepo

router = APIRouter()


# @require_verified
@router.post("/", response_model=dict)
@ensure_db_context
def post(create: GameNightCreate) -> dict:
    return _create_or_update(create).get_data(current_user_person_name())


# @require_verified
@router.put("/{id_}/", response_model=dict)
@ensure_db_context
def put(id_: int, update: GameNightUpdate) -> dict:
    return _create_or_update(update, id_).get_data(current_user_person_name())


# @require_admin
@router.delete("/{id_}/")
def delete(id_: int) -> None:
    GameNightRepo.delete_by_id(id_)


@router.get("/", response_model=List[dict])
@ensure_db_context
def get_many(limit: Optional[int] = None) -> List[dict]:
    if limit is None:
        gamenights = [gn for gn in GameNight.query()]
        all_votes = [vote for vote in Vote.query()]
    else:
        gamenights = [gn for gn in GameNight.query().order(-GameNight.date).fetch(int(limit))]
        gamenight_keys = [gn.key for gn in gamenights]
        if gamenight_keys:
            all_votes = [vote for vote in Vote.query(Vote.game_night.IN(gamenight_keys))]
        else:
            all_votes = []
    return [gn.get_data(current_user_person_name(), all_votes) for gn in gamenights]


@router.get("/{id_}/", response_model=dict)
@ensure_db_context
def get_one(id_: int) -> dict:
    if game_night := GameNightRepo.get_one_or_none(id_):
        return game_night.get_data(current_user_person_name())
    else:
        raise HTTPException(status_code=404)


def _create_or_update(
    input_: Union[GameNightCreate, GameNightUpdate],
    id_: Optional[int] = None,
) -> GameNight:
    # Create/Load GameNight
    if isinstance(input_, GameNightCreate):
        game_night = GameNight()
    elif isinstance(input_, GameNightUpdate) and id_:
        game_night = GameNightRepo.get(id_)
    else:
        raise Exception(f"Invalid input, input_ type '{type(input_)}' and {id_=}")

    # Update GameNight
    game_night.date = input_.date
    game_night.host = input_.host
    game_night.description = input_.description
    game_night.put()  # Ensures we have a key

    # Create/Update Votes
    if not game_night.completely_voted():
        for vote_input in input_.votes:
            if not Person.query(
                Person.name == vote_input.voter, Person.activated == True  # noqa
            ).get():
                raise HTTPException(status_code=400, detail="Deactivated person")
            if vote_input.voter == input_.host:
                continue

            if isinstance(vote_input, VoteCreate):
                vote = Vote()
                vote.game_night = game_night.key
                vote.voter = vote_input.voter
            elif isinstance(vote_input, VoteUpdate):
                vote = Vote.get_by_id(vote_input.id)
            else:
                raise Exception(f"Unknown type '{type(vote_input)}'")

            if vote_input.voter == current_user_person_name():  # Only allow vote for self
                vote.present = vote_input.present
                vote.appetizer = vote_input.appetizer
                vote.main_course = vote_input.main_course
                vote.dessert = vote_input.dessert
                vote.game = vote_input.game
            vote.put()

    # Calculate sum after vote changes
    if weighed_votes := [vote.weighed_sum() for vote in VoteRepo.get_many_by_present(game_night)]:
        game_night.sum = sum(weighed_votes) / len(weighed_votes)
        game_night.put()

    return game_night
