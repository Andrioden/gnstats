from google.cloud import ndb

person_names_allowed = ['Stian', 'André', 'Ole', 'Damian', 'Øivind']


class Person(ndb.Model):
    google_account_id = ndb.StringProperty(required=True)
    google_email = ndb.StringProperty()
    google_picture_url = ndb.StringProperty()
    name = ndb.StringProperty(required=True, choices=person_names_allowed)
    activated = ndb.BooleanProperty(required=True, default=True)
    avatar = ndb.BlobProperty()
    admin = ndb.BooleanProperty(default=False)

    @staticmethod
    def api_get_available_names():
        person_names_taken = [person.name for person in Person.query()]
        return [name for name in person_names_allowed if name not in person_names_taken]

    def get_data(self):
        return {
            'id': self.key.id(),
            'name': self.name,
            'activated': self.activated,
            'avatar': self.avatar is not None
        }
