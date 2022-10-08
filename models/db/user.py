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

    def get_data(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "activated": self.activated,
            "picture_url": self.google_picture_url,
        }

    def __repr__(self) -> str:
        return self.name
