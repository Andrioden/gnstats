from typing import List, Optional, Union

from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from api.session import me_activated_or_401, me_admin_or_401, me_or_none
from models.api.game_night import GameNightCreate, GameNightUpdate
from models.api.vote import VoteCreate, VoteUpdate
from models.db.game_night import GameNight, Vote
from models.db.user import User
from repos.game_night import GameNightRepo
from repos.user import UserRepo
from repos.vote import VoteRepo
from utils.db import ensure_db_context

router = APIRouter()


@router.post("/")
@ensure_db_context
def post(create: GameNightCreate, me: User = Depends(me_activated_or_401)) -> dict:
    return _create_or_update(me, create).get_data(me_name=me.name)


@router.put("/{id_}/")
@ensure_db_context
def put(id_: int, update: GameNightUpdate, me: User = Depends(me_activated_or_401)) -> dict:
    return _create_or_update(me, update, id_).get_data(me_name=me.name)


@router.delete("/{id_}/", dependencies=[Depends(me_admin_or_401)])
@ensure_db_context
def delete(id_: int) -> None:
    GameNightRepo.delete_by_id(id_)


@router.get("/")
@ensure_db_context
def get_many(me: Optional[User] = Depends(me_or_none)) -> List[dict]:
    all_votes = VoteRepo.get_all()
    return [
        gn.get_data(
            me_name=me.name if me else None,
            votes=all_votes,
        )
        for gn in GameNightRepo.get_all()
    ]


@router.get("/{id_}/")
@ensure_db_context
def get_one(id_: int, me: User = Depends(me_or_none)) -> dict:
    if game_night := GameNightRepo.get_one_or_none(id_):
        return game_night.get_data(me_name=me.name if me else None)
    else:
        raise HTTPException(HTTP_404_NOT_FOUND)


@router.post("/actions/recalculate-sum/", dependencies=[Depends(me_admin_or_401)])
@ensure_db_context
def post_recalculate_sums() -> None:
    for game_night in GameNightRepo.get_all():
        _update_sum_if_needed(game_night)


def _create_or_update(
    me: User,
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
    game_night.round_start = input_.round_start
    game_night.put()  # Ensures we have a key

    # Create/Update Votes
    if not game_night.completely_voted():
        for vote_input in input_.votes:
            if not UserRepo.exists(name=vote_input.voter, activated=True):
                raise HTTPException(HTTP_400_BAD_REQUEST, "Deactivated user")
            if vote_input.voter == input_.host:
                continue

            if isinstance(vote_input, VoteCreate):
                vote = Vote()
                vote.game_night = game_night.key
                vote.voter = vote_input.voter
            elif isinstance(vote_input, VoteUpdate):
                vote = VoteRepo.get(vote_input.id)
            else:
                raise Exception(f"Unknown type '{type(vote_input)}'")

            if vote_input.voter == me.name:  # Only allow vote for self
                vote.present = vote_input.present
                vote.appetizer = vote_input.appetizer
                vote.main_course = vote_input.main_course
                vote.dessert = vote_input.dessert
                vote.game = vote_input.game
            vote.put()

    # Calculate sum after vote changes
    _update_sum_if_needed(game_night)

    return game_night


def _update_sum_if_needed(game_night: GameNight) -> None:
    weighed_votes = [vote.weighed_sum() for vote in VoteRepo.get_many_by_present(game_night.key)]

    if weighed_votes:
        new_sum = sum(weighed_votes) / len(weighed_votes)
    else:
        new_sum = None

    if game_night.sum != new_sum:
        game_night.sum = new_sum
        game_night.put()
