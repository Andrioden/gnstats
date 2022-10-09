from typing import List, Optional

from google.cloud.ndb import BooleanProperty, DateProperty, FloatProperty, StringProperty

from models.db.base import DbModelBase
from models.db.user import ALLOWED_NAMES
from models.db.vote import Vote
from repos.vote import VoteRepo
from utils.date import date_to_epoch


class GameNight(DbModelBase):
    date = DateProperty(required=True)
    host = StringProperty(required=True, choices=ALLOWED_NAMES)
    description = StringProperty(required=True)
    round_start = BooleanProperty(default=False)
    sum = FloatProperty(default=None)

    def get_data(self, me_name: str, votes: Optional[List[Vote]] = None) -> dict:
        if votes is None:
            votes = [vote for vote in VoteRepo.get_many(self.key)]
        else:
            votes = [vote for vote in votes if vote.game_night == self.key]
        completed_votes = len([vote for vote in votes if not vote.completed_vote()]) == 0

        return {
            "id": self.id,
            "host": self.host,
            "date_epoch": date_to_epoch(self.date) if self.date else None,
            "description": self.description,
            "round_start": self.round_start,
            "sum": self.sum if completed_votes else 0,
            "votes": [
                vote.get_data() for vote in votes if (vote.voter == me_name or completed_votes)
            ],
            "not_voted": [vote.voter for vote in votes if not vote.completed_vote()],
            "own_vote": next((vote.get_data() for vote in votes if vote.voter == me_name), None),
            "completely_voted": completed_votes,
        }

    def completely_voted(self) -> bool:
        votes = [vote for vote in Vote.query(Vote.game_night == self.key)]
        if len(votes) == 0:  # Just created
            return False
        else:
            return len([vote for vote in votes if not vote.completed_vote()]) == 0
