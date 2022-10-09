from typing import List, Optional

from google.cloud.ndb import Key

from models.db.game_night import Vote
from repos import NotFoundError


class VoteRepo:
    @classmethod
    def count_all(cls) -> int:
        return Vote.query().count()

    @classmethod
    def get(cls, id_: int) -> Vote:
        if vote := Vote.get_by_id(id_):
            return vote
        else:
            raise NotFoundError(f"No {Vote.__name__} found")

    @classmethod
    def get_one_or_none(cls, id_: int) -> Optional[Vote]:
        return Vote.get_by_id(id_)

    @classmethod
    def get_all(cls) -> List[Vote]:
        return Vote.query().fetch()

    @classmethod
    def get_all_present(cls) -> List[Vote]:
        return Vote.query(Vote.present == True).fetch()  # noqa: E712

    @classmethod
    def get_many_by_present(cls, game_night_key: Key) -> List[Vote]:
        return Vote.query(Vote.game_night == game_night_key, Vote.present == True).fetch()  # noqa
