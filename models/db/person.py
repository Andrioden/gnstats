from typing import List

from google.cloud.ndb import BooleanProperty, StringProperty

from models.db.base import DbModelBase

person_names_allowed = ["Stian", "André", "Ole", "Damian", "Øivind"]


class Person(DbModelBase):
    google_id = StringProperty(required=True)
    google_email = StringProperty()
    google_picture_url = StringProperty()
    name = StringProperty(required=True, choices=person_names_allowed)
    activated = BooleanProperty(required=True, default=False)
    admin = BooleanProperty(default=False)

    @staticmethod
    def api_get_available_names() -> List[str]:
        person_names_taken = [person.name for person in Person.query()]
        return [name for name in person_names_allowed if name not in person_names_taken]

    def get_data(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "activated": self.activated,
            "picture_url": self.google_picture_url,
        }
