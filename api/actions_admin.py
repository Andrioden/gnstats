#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import webapp2
import json
from google.appengine.ext import ndb
from models import GameNight, Vote, person_names_allowed
from api.utils import *
from datetime import datetime
import logging


class ImportDataHandler(webapp2.RequestHandler):
    def get(self):

        self._clean_db()

        with open('data.csv', 'rb') as csv_file:
            for row in csv.reader(csv_file):
                logging.info(row)

                # DATA CLEANER - Host
                if row[2] == "Andre":
                    host = u'André'
                else:
                    host = row[2]

                # DATA CLEANER - Date
                date = self._attempt_to_convert_string_to_date(row[0], '%d %b %Y')
                if date is None:
                    date = self._attempt_to_convert_string_to_date(row[0], '%d/%m/%Y')
                if date is None:
                    date = self._attempt_to_convert_string_to_date(row[0], '%d.%m.%Y')

                # ADD DATA
                gn = GameNight(
                    date=date,
                    host=host,
                    description=row[1],
                    sum=0
                )
                gn.put()

                for person_name in person_names_allowed:
                    if person_name == host:
                        continue
                    elif person_name == u'André':
                        vote = self._create_and_get_vote_object(row, gn.key, u'André', 3)
                    elif person_name == "Damian":
                        vote = self._create_and_get_vote_object(row, gn.key, u'Damian', 7)
                    elif person_name == "Stian":
                        vote = self._create_and_get_vote_object(row, gn.key, u'Stian', 11)
                    elif person_name == "Ole":
                        vote = self._create_and_get_vote_object(row, gn.key, u'Ole', 15)
                    if vote:
                        gn.sum += vote.weighed_sum()

                gn.put()

        set_json_response(self.response, {'response': "OK"})

    @staticmethod
    def _clean_db():
        ndb.delete_multi(GameNight.query().fetch(keys_only=True))
        ndb.delete_multi(Vote.query().fetch(keys_only=True))

    @staticmethod
    def _attempt_to_convert_string_to_date(date_string, date_format):
        try:
            return datetime.strptime(date_string, date_format)
        except Exception:
            return None

    @staticmethod
    def _create_and_get_vote_object(row, game_night_key, voter, start_column):
        vote = Vote(
            game_night=game_night_key,
            voter=voter,
            appetizer=int(row[start_column]),
            main_course=int(row[start_column+1]),
            dessert=int(row[start_column+2]),
            game=int(row[start_column+3])
        )
        vote.put()
        return vote


app = webapp2.WSGIApplication([
    (r'/api/actions/admin/importdata/', ImportDataHandler)
], debug=True)