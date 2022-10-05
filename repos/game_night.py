from typing import Optional

from google.cloud.ndb import Key, delete_multi

from models.db.game_night import GameNight
from models.db.vote import Vote
from repos import NotFoundError


class GameNightRepo:
    @classmethod
    def delete_by_id(cls, id_: int) -> None:
        game_night_key = Key(GameNight, id_)
        delete_multi(Vote.query(Vote.game_night == game_night_key).fetch(keys_only=True))
        game_night_key.delete()  # type: ignore[union-attr]

    @classmethod
    def count_all(cls) -> int:
        return GameNight.query().count()

    @classmethod
    def get(cls, id_: int) -> GameNight:
        if game_night := GameNight.get_by_id(id_):
            return game_night  # type: ignore
        else:
            raise NotFoundError(f"No {GameNight.__name__} found")

    @classmethod
    def get_one_or_none(cls, id_: int) -> Optional[GameNight]:
        return GameNight.get_by_id(id_)  # type: ignore