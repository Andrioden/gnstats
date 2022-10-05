from typing import List, Optional

from models.db.person import Person
from models.external.google import GoogleUser
from repos import IntegrityError, NotFoundError


class PersonRepo:
    @classmethod
    def create(cls, user: GoogleUser, name: str) -> Person:
        if cls.get_one_or_none_by_google_id(user.sub):
            raise IntegrityError(f"User {user.sub=} connected to another Person")

        person = Person(
            google_id=user.sub,
            google_email=user.email,
            google_picture_url=user.picture,
            name=name,
        )
        person.put()
        return person

    @classmethod
    def update_activated(cls, id_: int, value: bool) -> Person:
        person = cls.get(id_)
        person.activated = value
        person.put()
        return person

    @classmethod
    def get(cls, id_: int) -> Person:
        if person := Person.get_by_id(id_):
            return person
        else:
            raise NotFoundError(f"No {Person.__name__} found")

    @classmethod
    def get_one_or_none_by_google_id(cls, id_: str) -> Optional[Person]:
        return Person.query(Person.google_id == id_).get()

    @classmethod
    def get_one_or_none_by_name(cls, name: str) -> Optional[Person]:
        return Person.query(Person.name == name).get()

    @classmethod
    def get_all(cls) -> List[Person]:
        return Person.query().fetch()

    @classmethod
    def delete(cls, person: Person) -> None:
        person.key.delete()
