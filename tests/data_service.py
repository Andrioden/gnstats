from models import GameNight


class DataService:
    @staticmethod
    def create_game_night() -> GameNight:
        game_night = GameNight(host="Stian", description="test")
        game_night.put()
        return game_night
