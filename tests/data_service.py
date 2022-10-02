from typing import Optional

from models.db.game_night import GameNight
from models.db.person import Person
from models.db.vote import Vote


class DataService:
    @staticmethod
    def ensure_person(name: str) -> Person:
        if person := Person.query(Person.name == name).get():
            return person
        else:
            person = Person(
                userid="test",
                nickname="nick",
                name=name,
            )
            person.put()
            return person

    @staticmethod
    def create_game_night() -> GameNight:
        game_night = GameNight(host="Stian", description="test")
        game_night.put()
        return game_night

    @staticmethod
    def create_vote(game_night: GameNight, voter: str = "André", appetizer: Optional[int] = None) -> Vote:
        vote = Vote(
            game_night=game_night.key,
            voter=DataService.ensure_person(voter).name,
            appetizer=appetizer
        )
        vote.put()
        return vote
