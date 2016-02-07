#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
from datetime import datetime, date, timedelta
import logging


persons = ['Stian', 'André', 'Ole', 'Damian']


class GameNight(ndb.Model):
    host = ndb.StringProperty(required=True, choices=persons)
    date = ndb.DateProperty(required=True)
    description = ndb.StringProperty(required=True)
    sum = ndb.IntegerProperty()


def _validate_dice(prop, value):
    if value not in [1, 2, 3, 4, 5, 6]:
        raise Exception("Value %s for %s not a dice number." % (value, prop))
    else:
        return value


class Vote(ndb.Model):
    date = ndb.DateProperty(default=datetime.now())
    voter = ndb.StringProperty(required=True, choices=persons)
    appetizer = ndb.IntegerProperty(required=True, validator=_validate_dice)
    main_course = ndb.IntegerProperty(required=True, validator=_validate_dice)
    dessert = ndb.IntegerProperty(required=True, validator=_validate_dice)
    game = ndb.IntegerProperty(required=True, validator=_validate_dice)


