#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
from datetime import datetime, date, timedelta
import logging
from config import *


person_names = [u'Stian', u'André', u'Ole', u'Damian']


class Person(ndb.Model):
    name = ndb.StringProperty(required=True, choices=person_names)
    userid = ndb.StringProperty(required=True)
    nickname = ndb.StringProperty(required=True)


class GameNight(ndb.Model):
    date = ndb.DateProperty()
    host = ndb.StringProperty(required=True, choices=person_names)
    description = ndb.StringProperty(required=True)
    sum = ndb.FloatProperty(default=0)

    def get_data(self, query_person_name=None):
        votes = [vote for vote in Vote.query(Vote.game_night == self.key)]
        data = {
            'id': self.key.id(),
            'host': self.host,
            'date_epoch': _date_to_epoch(self.date) if self.date else None,
            'description': self.description,
            'sum': round(self.sum, 1),
            'votes': [vote.get_data() for vote in votes],
            'own_vote': next((vote.get_data() for vote in votes if vote.voter == query_person_name), None),
            'completely_voted': len([vote for vote in votes if not vote.complete_vote()]) == 0
        }
        return data


def _validate_dice(prop, value):
    if value not in [1, 2, 3, 4, 5, 6]:
        raise Exception("Value %s for %s not a dice number." % (value, prop))
    else:
        return value


class Vote(ndb.Model):
    game_night = ndb.KeyProperty(GameNight, required=True)
    date = ndb.DateProperty(default=datetime.now())
    voter = ndb.StringProperty(required=True, choices=person_names)
    appetizer = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    main_course = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    dessert = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])
    game = ndb.IntegerProperty(choices=[1, 2, 3, 4, 5, 6])

    def get_data(self):
        return {
            'id': self.key.id(),
            'voter': self.voter,
            'appetizer': self.appetizer,
            'main_course': self.main_course,
            'dessert': self.dessert,
            'game': self.game,
            'sum': self.weighed_sum(),
            'complete_vote': self.complete_vote()
        }

    def weighed_sum(self):
        weighed_sum = 0
        weighed_sum += self.appetizer * Weight_Appetizer if self.appetizer else 0
        weighed_sum += self.main_course * Weight_MainCourse if self.main_course else 0
        weighed_sum += self.dessert * Weight_Dessert if self.dessert else 0
        weighed_sum += self.game * Weight_Game if self.game else 0
        return weighed_sum

    def complete_vote(self):
        return None not in [self.appetizer, self.main_course, self.dessert, self.game]


def _date_to_epoch(date_value):
    return int((date_value - date(1970,1,1)).total_seconds())
