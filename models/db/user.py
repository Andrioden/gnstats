from typing import List

from google.cloud.ndb import BooleanProperty, StringProperty

from models.db.base import DbModelBase

ALLOWED_NAMES = ["Stian", "André", "Ole", "Damian", "Øivind"]


class User(DbModelBase):
    google_id = StringProperty(required=True)
    google_email = StringProperty()
    google_picture_url = StringProperty()
    name = StringProperty(required=True, choices=ALLOWED_NAMES)
    activated = BooleanProperty(required=True, default=False)
    admin = BooleanProperty(default=False)

    @staticmethod
    def api_get_available_names() -> List[str]:
        names_taken = [user.name for user in User.query()]
        return [name for name in ALLOWED_NAMES if name not in names_taken]

    def get_data(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "activated": self.activated,
            "picture_url": self.google_picture_url,
        }
