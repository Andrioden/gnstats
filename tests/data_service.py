from datetime import datetime
from typing import Optional

from models.db.game_night import GameNight
from models.db.user import User
from models.db.vote import Vote
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
        return cls.build_user(name="Ole", activated=True)

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
    def create_game_night(cls) -> GameNight:
        game_night = GameNight(date=datetime.now().date(), host="Stian", description="test")
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
            voter=DataService.create_user(voter).name,
            present=present,
            appetizer=appetizer,
        )
        vote.put()
        return vote
