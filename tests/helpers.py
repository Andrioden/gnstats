from google.cloud import ndb

from models.db.game_night import GameNight, Vote
from models.db.user import User


def clean_db() -> None:
    ndb.delete_multi(User.query().fetch(keys_only=True))
    ndb.delete_multi(Vote.query().fetch(keys_only=True))
    ndb.delete_multi(GameNight.query().fetch(keys_only=True))
