from typing import List

from google.cloud.ndb import BlobProperty, BooleanProperty, StringProperty

from models.db.base import DbModelBase

person_names_allowed = ["Stian", "André", "Ole", "Damian", "Øivind"]


class Person(DbModelBase):
    google_account_id = StringProperty(required=True)
    google_email = StringProperty()
    google_picture_url = StringProperty()
    name = StringProperty(required=True, choices=person_names_allowed)
    activated = BooleanProperty(required=True, default=True)
    avatar = BlobProperty()
    admin = BooleanProperty(default=False)

    @staticmethod
    def api_get_available_names() -> List[str]:
        person_names_taken = [person.name for person in Person.query()]
        return [name for name in person_names_allowed if name not in person_names_taken]

    def get_data(self):
        return {
            "id": self.key.id(),
            "name": self.name,
            "activated": self.activated,
            "avatar": self.avatar is not None,
        }
