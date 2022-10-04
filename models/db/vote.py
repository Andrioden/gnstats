from google.cloud import ndb

from config import Weight_Appetizer, Weight_Dessert, Weight_Game, Weight_MainCourse
from models.db.person import person_names_allowed


class Vote(ndb.Model):
    game_night = ndb.KeyProperty("GameNight", required=True)
    voter = ndb.StringProperty(required=True, choices=person_names_allowed)
    present = ndb.BooleanProperty(default=True)
    appetizer = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    main_course = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    dessert = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    game = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])

    def get_data(self):
        return {
            "id": self.key.id(),
            "voter": self.voter,
            "present": self.present,
            "appetizer": self.appetizer,
            "main_course": self.main_course,
            "dessert": self.dessert,
            "game": self.game,
            "sum": self.weighed_sum() if self.present else 0,
            "complete_vote": self.complete_vote(),
        }

    def appertizer_int(self):
        return self.appetizer if self.appetizer else 0

    def main_course_int(self):
        return self.main_course if self.main_course else 0

    def dessert_int(self):
        return self.dessert if self.dessert else 0

    def game_int(self):
        return self.game if self.game else 0

    def weighed_sum(self):
        sum = 0
        sum += self.appertizer_int() * Weight_Appetizer
        sum += self.main_course_int() * Weight_MainCourse
        sum += self.dessert_int() * Weight_Dessert
        sum += self.game_int() * Weight_Game
        return sum / (Weight_Appetizer + Weight_MainCourse + Weight_Dessert + Weight_Game)

    def nonweighed_sum(self):
        return self.appertizer_int() + self.main_course_int() + self.dessert_int() + self.game_int()

    def complete_vote(self):
        if self.present:
            return None not in [self.appetizer, self.main_course, self.dessert, self.game]
        else:
            return True
