from google.cloud.ndb import Model


class DbModelBase(Model):
    @property
    def id(self) -> int:
        return self.key.id()
