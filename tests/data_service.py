from typing import Optional

from models.db.game_night import GameNight
from models.db.person import Person
from models.db.vote import Vote
from repos.person import PersonRepo


class DataService:
    @classmethod
    def ensure_person(cls, name: str) -> Person:
        if person := PersonRepo.get_one_or_none_by_name(name):
            return person
        else:
            person = Person(
                google_account_id="fake",
                google_email="fake@fake.no",
                google_picture_url="http://www.fake.no/img/1",
                name=name,
            )
            person.put()
            return person

    @classmethod
    def ensure_person_deleted(cls, name: str) -> None:
        if person := PersonRepo.get_one_or_none_by_name(name):
            PersonRepo.delete(person)

    @classmethod
    def create_game_night(cls) -> GameNight:
        game_night = GameNight(host="Stian", description="test")
        game_night.put()
        return game_night

    @classmethod
    def create_vote(
        cls,
        game_night: Optional[GameNight] = None,
        voter: str = "André",
        present: bool = True,
        appetizer: Optional[int] = None,
    ) -> Vote:
        vote = Vote(
            game_night=game_night.key if game_night else cls.create_game_night().key,
            voter=DataService.ensure_person(voter).name,
            present=present,
            appetizer=appetizer,
        )
        vote.put()
        return vote
