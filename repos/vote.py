from typing import List

from models.db.game_night import GameNight
from models.db.vote import Vote
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
    def get_all_present(cls) -> List[Vote]:
        return Vote.query(Vote.present == True).fetch()  # noqa: E712

    @classmethod
    def get_many_by_present(cls, game_night: GameNight) -> List[Vote]:
        return Vote.query(Vote.game_night == game_night.key, Vote.present == True).fetch()  # noqa
