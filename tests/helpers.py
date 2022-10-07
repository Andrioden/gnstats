from google.cloud import ndb

from models.db.game_night import GameNight
from models.db.user import User
from models.db.vote import Vote


def clean_db() -> None:
    ndb.delete_multi(User.query().fetch(keys_only=True))
    ndb.delete_multi(Vote.query().fetch(keys_only=True))
    ndb.delete_multi(GameNight.query().fetch(keys_only=True))
