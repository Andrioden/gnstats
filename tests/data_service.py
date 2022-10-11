from datetime import datetime
from typing import Optional

from google.cloud.ndb import Key

from models.db.game_night import GameNight, Vote
from models.db.user import User
from models.external.google import GoogleAccount


class DataService:
    @classmethod
    def build_google_account(cls) -> GoogleAccount:
        return GoogleAccount(
            sub="1",
            email="and@and.no",
            email_verified=True,
            picture="https://www.pic.no/1",
            name="Jonas Store",
        )

    @classmethod
    def build_user(cls, name: str, activated: bool = False, admin: bool = False) -> User:
        return User(
            google_id="fake",
            google_email="fake@fake.no",
            google_picture_url="https://www.fake.no/img/1",
            name=name,
            activated=activated,
            admin=admin,
        )

    @classmethod
    def build_deactivated_user(cls) -> User:
        return cls.build_user(name="Ole", activated=False)

    @classmethod
    def build_activated_user(cls) -> User:
        return cls.build_user(name="Ole", activated=True)

    @classmethod
    def build_admin_user(cls) -> User:
        return cls.build_user(name="Ole", activated=True, admin=True)

    @classmethod
    def create_user(cls, name: str, activated: bool = True) -> User:
        user = cls.build_user(name=name, activated=activated)
        user.put()
        return user

    @classmethod
    def build_game_night(
        cls, id_: Optional[int] = None, host: str = "Stian", sum_: Optional[int] = None
    ) -> GameNight:
        return GameNight(
            key=Key(GameNight, id_) if id_ else None,
            date=datetime.now().date(),
            host=host,
            description="test",
            sum=sum_,
        )

    @classmethod
    def create_game_night(cls, sum_: Optional[int] = None) -> GameNight:
        game_night = cls.build_game_night(sum_=sum_)
        game_night.put()
        return game_night

    @classmethod
    def build_vote(
        cls,
        game_night: GameNight,
        voter: str = "André",
        present: bool = True,
        appetizer: Optional[int] = 1,
        main_course: Optional[int] = 1,
        dessert: Optional[int] = 1,
        game: Optional[int] = 1,
    ) -> Vote:
        return Vote(
            game_night=game_night.key,
            voter=DataService.create_user(voter).name,
            present=present,
            appetizer=appetizer,
            main_course=main_course,
            dessert=dessert,
            game=game,
        )

    @classmethod
    def create_vote(
        cls,
        game_night: Optional[GameNight] = None,
        voter: str = "André",
        present: bool = True,
        appetizer: Optional[int] = 1,
        main_course: Optional[int] = 1,
        dessert: Optional[int] = 1,
        game: Optional[int] = 1,
    ) -> Vote:
        vote = cls.build_vote(
            game_night=game_night if game_night else cls.create_game_night(),
            voter=voter,
            present=present,
            appetizer=appetizer,
            main_course=main_course,
            dessert=dessert,
            game=game,
        )
        vote.put()
        return vote
