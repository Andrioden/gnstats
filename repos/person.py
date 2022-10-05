from typing import List, Optional

from models.db.person import Person


class PersonRepo:
    @classmethod
    def get_one_or_none_by_name(cls, name: str) -> Optional[Person]:
        return Person.query(Person.name == name).get()

    @classmethod
    def get_all(cls) -> List[Person]:
        return Person.query().fetch()

    @classmethod
    def delete(cls, person: Person) -> None:
        person.key.delete()
