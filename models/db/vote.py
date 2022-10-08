from google.cloud.ndb import BooleanProperty, IntegerProperty, KeyProperty, StringProperty

from config import Weight_Appetizer, Weight_Dessert, Weight_Game, Weight_MainCourse
from models.db.base import DbModelBase
from models.db.user import ALLOWED_NAMES


class Vote(DbModelBase):
    game_night = KeyProperty("GameNight", required=True)
    voter = StringProperty(required=True, choices=ALLOWED_NAMES)
    present = BooleanProperty(default=True)
    appetizer = IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    main_course = IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    dessert = IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    game = IntegerProperty(choices=[1, 2, 3, 4, 5, 6])

    def get_data(self) -> dict:
        return {
            "id": self.id,
            "voter": self.voter,
            "present": self.present,
            "appetizer": self.appetizer,
            "main_course": self.main_course,
            "dessert": self.dessert,
            "game": self.game,
            "sum": self.weighed_sum() if self.present else 0,
            "completed_vote": self.completed_vote(),
        }

    def appetizer_int(self) -> int:
        return self.appetizer if self.appetizer else 0

    def main_course_int(self) -> int:
        return self.main_course if self.main_course else 0

    def dessert_int(self) -> int:
        return self.dessert if self.dessert else 0

    def game_int(self) -> int:
        return self.game if self.game else 0

    def weighed_sum(self) -> float:
        sum_ = 0.0
        sum_ += self.appetizer_int() * Weight_Appetizer
        sum_ += self.main_course_int() * Weight_MainCourse
        sum_ += self.dessert_int() * Weight_Dessert
        sum_ += self.game_int() * Weight_Game
        return sum_ / (Weight_Appetizer + Weight_MainCourse + Weight_Dessert + Weight_Game)

    def nonweighed_sum(self) -> int:
        return self.appetizer_int() + self.main_course_int() + self.dessert_int() + self.game_int()

    def completed_vote(self) -> bool:
        if self.present:
            return None not in [self.appetizer, self.main_course, self.dessert, self.game]
        else:
            return True
