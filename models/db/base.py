from google.cloud.ndb import Model


class DbModelBase(Model):  # type: ignore[misc]
    @property
    def id(self) -> int:
        return self.key.id()
