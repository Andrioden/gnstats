#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import webapp2
import json
from google.appengine.ext import ndb
from models import GameNight, Vote, person_names_allowed
from api.utils import *
from datetime import datetime, date
import logging


class DataImportPythonScript(webapp2.RequestHandler):
    def get(self):

        if not validate_logged_in_admin(self.response):
            return

        self.response.out.write("# FULL PYTHON SCRIPT: <br/>")
        self.response.out.write("<br/>")

        self.response.out.write("# IMPORTS: <br/>")
        self.response.out.write("from models import * <br/>")
        self.response.out.write("from datetime import datetime, date <br/>")
        self.response.out.write("from google.appengine.ext import ndb <br/>")
        self.response.out.write("<br/>")

        self.response.out.write("# CLEAR DB: <br/>")
        self.response.out.write("ndb.delete_multi(GameNight.query().fetch(keys_only=True)) <br/>")
        self.response.out.write("ndb.delete_multi(Vote.query().fetch(keys_only=True)) <br/>")

        self.response.out.write("<br/>")
        self.response.out.write("# GameNights: <br/>")
        for player in GameNight.query().fetch():
            self.response.out.write(self._get_data_dump_string_of_object(player) + "<br><br>")

        self.response.out.write("<br/>")
        self.response.out.write("# Votes: <br/>")
        for rule in Vote.query().fetch():
            self.response.out.write(self._get_data_dump_string_of_object(rule) + "<br><br>")

        # Uncomment below to download as file, not really practical but keeping code
        #self.response.headers['Content-Type'] = 'text/csv'
        #self.response.headers['Content-Disposition'] = "attachment; filename=siage_import_script.py"


    def _get_data_dump_string_of_object(self, obj):
        data_string = "%s(id=%s, " % (type(obj).__name__, obj.key.id())
        for variable_name in obj.__dict__['_values'].keys():  # __dict__['_values'] contains all class object variables
            variable_value = getattr(obj, variable_name, None)
            if variable_value is None:
                data_string += "%s=None, " % variable_name
            elif type(variable_value) is list:
                continue
            elif type(variable_value) in (int, long, bool, float):
                data_string += "%s=%s, " % (variable_name, variable_value)
            elif type(variable_value) is unicode:
                escaped_value = variable_value.replace("\'", "\\'").replace("\"", "\\\"")
                data_string += "%s=u'%s', " % (variable_name, escaped_value)
            elif type(variable_value) is date:
                data_string += "%s=date.fromtimestamp(%s), " % (variable_name, date_to_epoch(variable_value))
            elif type(variable_value) is datetime:
                data_string += "%s=datetime.fromtimestamp(%s), " % (variable_name, date_to_epoch(variable_value))
            elif type(variable_value) is ndb.Key:
                data_string += "%s=ndb.Key(%s, %s), " % (variable_name, variable_value.kind(), variable_value.id())
            else:
                raise Exception("Type not handled: " + type(variable_value).__name__)

        data_string = data_string[:-2]
        data_string += ").put()"
        return data_string


class RunImportPythonScript(webapp2.RequestHandler):
    def get(self):
        # Paste generated script from DataImportPythonScript here and run it in dev
        pass


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
    (r'/api/actions/admin/dataimportpythonscript/', DataImportPythonScript),
    (r'/api/actions/admin/runimportpythonscript/', RunImportPythonScript),
    (r'/api/actions/admin/importdata/', ImportDataHandler)
], debug=True)