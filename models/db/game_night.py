from google.cloud.ndb import DateProperty, FloatProperty, StringProperty

from models.db.base import DbModelBase
from models.db.person import person_names_allowed
from models.db.vote import Vote
from utils.date import date_to_epoch


class GameNight(DbModelBase):
    date = DateProperty()
    host = StringProperty(required=True, choices=person_names_allowed)
    description = StringProperty(required=True)
    sum = FloatProperty(default=0)

    def get_data(self, query_person_name=None, votes=None) -> dict:
        if votes is None:
            votes = [vote for vote in Vote.query(Vote.game_night == self.key)]
        else:
            votes = [vote for vote in votes if vote.game_night == self.key]
        completely_voted = len([vote for vote in votes if not vote.complete_vote()]) == 0

        return {
            "id": self.id,
            "host": self.host,
            "date_epoch": date_to_epoch(self.date) if self.date else None,
            "description": self.description,
            "sum": self.sum if completely_voted else 0,
            "votes": [
                vote.get_data()
                for vote in votes
                if (vote.voter == query_person_name or completely_voted)
            ],
            "not_voted": [vote.voter for vote in votes if not vote.complete_vote()],
            "own_vote": next(
                (vote.get_data() for vote in votes if vote.voter == query_person_name), None
            ),
            "completely_voted": completely_voted,
        }

    def completely_voted(self) -> bool:
        votes = [vote for vote in Vote.query(Vote.game_night == self.key)]
        if len(votes) == 0:  # Just created
            return False
        else:
            return len([vote for vote in votes if not vote.complete_vote()]) == 0
