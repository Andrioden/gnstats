from typing import Optional

from models.db.game_night import GameNight
from models.db.person import Person
from models.db.vote import Vote
from models.external.google import GoogleUser


class DataService:
    @classmethod
    def build_user(cls) -> GoogleUser:
        return GoogleUser(
            sub="1",
            email="and@and.no",
            email_verified=True,
            picture="https://www.pic.no/1",
            name="Jonas Store",
        )

    @classmethod
    def build_person(cls, name: str, activated: bool = False, admin: bool = False) -> Person:
        return Person(
            google_id="fake",
            google_email="fake@fake.no",
            google_picture_url="http://www.fake.no/img/1",
            name=name,
            activated=activated,
            admin=admin,
        )

    @classmethod
    def build_deactivated_person(cls) -> Person:
        return cls.build_person(name="Ole", activated=True)

    @classmethod
    def build_activated_person(cls) -> Person:
        return cls.build_person(name="Ole", activated=True)

    @classmethod
    def build_admin_person(cls) -> Person:
        return cls.build_person(name="Ole", activated=True, admin=True)

    @classmethod
    def create_person(cls, name: str, activated: bool = True) -> Person:
        person = cls.build_person(name=name, activated=activated)
        person.put()
        return person

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
            voter=DataService.create_person(voter).name,
            present=present,
            appetizer=appetizer,
        )
        vote.put()
        return vote
