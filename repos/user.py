from typing import List, Optional

from models.db.user import User
from models.external.google import GoogleAccount
from repos import IntegrityError, NotFoundError


class UserRepo:
    @classmethod
    def create(cls, google_acc: GoogleAccount, name: str) -> User:
        if cls.get_one_or_none_by_google_id(google_acc.sub):
            raise IntegrityError(f"Google account {google_acc.sub=} connected to another user")

        user = User(
            google_id=google_acc.sub,
            google_email=google_acc.email,
            google_picture_url=google_acc.picture,
            name=name,
        )
        user.put()
        return user

    @classmethod
    def update_activated(cls, id_: int, value: bool) -> User:
        user = cls.get(id_)
        user.activated = value
        user.put()
        return user

    @classmethod
    def get(cls, id_: int) -> User:
        if user := User.get_by_id(id_):
            return user
        else:
            raise NotFoundError(f"No {User.__name__} found")

    @classmethod
    def get_one_or_none_by_google_id(cls, id_: str) -> Optional[User]:
        return User.query(User.google_id == id_).get()

    @classmethod
    def get_one_or_none_by_name(cls, name: str) -> Optional[User]:
        return User.query(User.name == name).get()

    @classmethod
    def get_all(cls) -> List[User]:
        return User.query().fetch()

    @classmethod
    def delete(cls, user: User) -> None:
        user.key.delete()
