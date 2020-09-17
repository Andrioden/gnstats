#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
from datetime import datetime, date, timedelta
import logging
from config import *


person_names_allowed = [u'Stian', u'André', u'Ole', u'Damian', u'Øivind']


class Person(ndb.Model):
    userid = ndb.StringProperty(required=True) # Google userid
    nickname = ndb.StringProperty(required=True) # Google nickname
    name = ndb.StringProperty(required=True, choices=person_names_allowed)
    activated = ndb.BooleanProperty(required=True, default=True)
    avatar = ndb.BlobProperty()

    def get_data(self):
        return {
            'id': self.key.id(),
            'name': self.name,
            'activated': self.activated
        }


class GameNight(ndb.Model):
    date = ndb.DateProperty()
    host = ndb.StringProperty(required=True, choices=person_names_allowed)
    description = ndb.StringProperty(required=True)
    sum = ndb.FloatProperty(default=0)

    def get_data(self, query_person_name=None, _cached_votes=None):
        if _cached_votes is None:
            votes = [vote for vote in Vote.query(Vote.game_night == self.key)]
        else:
            votes = [vote for vote in _cached_votes if vote.game_night == self.key]
        completely_voted = len([vote for vote in votes if not vote.complete_vote()]) == 0

        return {
            'id': self.key.id(),
            'host': self.host,
            'date_epoch': _date_to_epoch(self.date) if self.date else None,
            'description': self.description,
            'sum': self.sum if completely_voted else 0,
            'votes': [vote.get_data() for vote in votes if (vote.voter == query_person_name or completely_voted)],
            'not_voted': [vote.voter for vote in votes if not vote.complete_vote()],
            'own_vote': next((vote.get_data() for vote in votes if vote.voter == query_person_name), None),
            'completely_voted': completely_voted
        }

    def completely_voted(self):
        votes = [vote for vote in Vote.query(Vote.game_night == self.key)]
        if len(votes) == 0: # Just created
            return False
        else:
            return len([vote for vote in votes if not vote.complete_vote()]) == 0

    def calculate_and_save_sum(self):
        weighed_votes = [vote.weighed_sum() for vote in Vote.query(Vote.game_night == self.key, Vote.present == True)]
        self.sum = sum(weighed_votes) / len(weighed_votes)
        self.put()


class Vote(ndb.Model):
    game_night = ndb.KeyProperty(GameNight, required=True)
    date = ndb.DateProperty(default=datetime.now())
    voter = ndb.StringProperty(required=True, choices=person_names_allowed)
    present = ndb.BooleanProperty(default=True)
    appetizer = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    main_course = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    dessert = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    game = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])

    def get_data(self):
        return {
            'id': self.key.id(),
            'voter': self.voter,
            'present': self.present,
            'appetizer': self.appetizer,
            'main_course': self.main_course,
            'dessert': self.dessert,
            'game': self.game,
            'sum': self.weighed_sum() if self.present else 0,
            'complete_vote': self.complete_vote()
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


def _date_to_epoch(date_value):
    return int((date_value - date(1970, 1, 1)).total_seconds())
