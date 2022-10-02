from google.cloud import ndb

person_names_allowed = ['Stian', 'André', 'Ole', 'Damian', 'Øivind']


class Person(ndb.Model):
    userid = ndb.StringProperty(required=True)  # Google userid
    nickname = ndb.StringProperty(required=True)  # Google nickname
    name = ndb.StringProperty(required=True, choices=person_names_allowed)
    activated = ndb.BooleanProperty(required=True, default=True)
    avatar = ndb.BlobProperty()

    def get_data(self):
        return {
            'id': self.key.id(),
            'name': self.name,
            'activated': self.activated,
            'avatar': self.avatar is not None
        }
