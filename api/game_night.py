#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import json
import logging
from datetime import datetime
from models import *
from google.appengine.api import users
from utils import *


class GameNightsHandler(webapp2.RequestHandler):
    def get(self):
        data = [game_night.get_data() for game_night in GameNight.query()]
        set_json_response(self.response, data)


class SyncHandler(webapp2.RequestHandler):
    def put(self):
        if not validate_authenticated(self.response):
            return

        request_data = json.loads(self.request.body)
        logging.info(request_data)

        return_data = []
        for updated_game_night in request_data:

            if not validate_request_data(self.response, updated_game_night, ['host', 'date', 'description']):
                return

            gn = self._get_or_create_game_night_object(updated_game_night.get('id'))

            gn.date = datetime.strptime(updated_game_night['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            gn.host = updated_game_night['host']
            gn.description = updated_game_night['description']
            gn.sum = 0
            gn.put()

            for vote_data in updated_game_night['votes']:
                if not vote_data['voter'] == updated_game_night['host']:
                    if vote_data.has_key('id'):
                        vote = Vote.get_by_id(int(vote_data['id']))
                    else:
                        vote = Vote()

                    vote.game_night = gn.key
                    vote.voter = vote_data['voter']
                    vote.appetizer = vote_data.get('appetizer')
                    vote.main_course = vote_data.get('main_course')
                    vote.dessert = vote_data.get('dessert')
                    vote.game = vote_data.get('game')
                    vote.put()

                    gn.sum += vote.weighed_sum()

            gn.put()

            return_data.append({
                'index': updated_game_night['index'],
                'id': gn.key.id(),
                'sum': round(gn.sum, 1)
            })

        set_json_response(self.response, return_data)

    @staticmethod
    def _get_or_create_game_night_object(id):
        if id:
            return GameNight.get_by_id(int(id))
        else:
            return GameNight()


app = webapp2.WSGIApplication([
    (r'/api/game_night/', GameNightsHandler),
    (r'/api/game_night/sync', SyncHandler)
], debug=True)
