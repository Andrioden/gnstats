#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import json
import logging
from datetime import datetime
from models import *
from google.appengine.api import users
from utils import *
from decorators import *


class GameNightsHandler(webapp2.RequestHandler):
    def get(self):
        limit = self.request.get("limit", None)
        if limit is None:
            gamenights = [gn for gn in GameNight.query()]
            all_votes = [vote for vote in Vote.query()]
        else:
            gamenights = [gn for gn in GameNight.query().order(-GameNight.date).fetch(int(limit))]
            gamenight_keys = [gn.key for gn in gamenights]
            all_votes = [vote for vote in Vote.query(Vote.game_night.IN(gamenight_keys))]
        data = [gn.get_data(current_user_person_name(), all_votes) for gn in gamenights]
        set_json_response(self.response, data)

    @require_verified
    @require_request_data(['host', 'date', 'description'])
    def post(self):
        game_night = _create_or_update(self)
        if game_night is None:
            return
        else:
            set_json_response(self.response, {'id': game_night.key.id()})


class GameNightHandler(webapp2.RequestHandler):
    def get(self, gn_id):
        gn = GameNight.get_by_id(int(gn_id))
        if gn is None:
            self.abort(404)
        else:
            votes = [vote for vote in Vote.query(Vote.game_night == gn.key)]
            data = gn.get_data(current_user_person_name(), votes)
            set_json_response(self.response, data)

    @require_verified
    @require_request_data(['host', 'date', 'description'])
    def put(self, gn_id):
        game_night = _create_or_update(self, gn_id)
        if game_night is None:
            return
        else:
            set_json_response(self.response, {'response': "OK"})

    @require_admin
    def delete(self, gn_id):
        gn_key = GameNight.get_by_id(int(gn_id)).key
        ndb.delete_multi(Vote.query(Vote.game_night == gn_key).fetch(keys_only=True))
        gn_key.delete()

        set_json_response(self.response, {'response': "OK"})


def _create_or_update(request_handler, gn_id = None):
    request_data = json.loads(request_handler.request.body)

    # Create/Update GameNight
    if gn_id is not None:
        game_night = GameNight.get_by_id(int(gn_id))
    else:
        game_night = GameNight()

    # We need to use an dateOnly field because the date field is localized by the client, which works bad when we are only saving date and not time to db
    # When we are not saving localized time we cant transfer it back to the client with correct localized date
    # So when you register a game night in Norway (GMT+1) at 0030 it is converted to 2330 previous day.
    game_night.date = datetime.strptime(request_data['dateOnly'], '%d/%m/%Y')

    game_night.host = request_data['host']
    game_night.description = request_data['description']

    if gn_id is None: # To get an ID for vote(s)
        game_night.put()

    if not game_night.completely_voted():
        for vote_data in request_data['votes']:
            if vote_data['voter'] == request_data['host']:
                continue

            if not Person.query(Person.name == vote_data['voter']).get().activated:
                error(400, request_handler.response, "ERROR_INACTIVE_CANT_VOTE", "Deactivated person is not allowed to vote!")
                return None

            if vote_data.has_key('id'):
                vote_id = int(vote_data['id'])
                vote = Vote.get_by_id(vote_id)
            else:
                vote = Vote()

            vote.game_night = game_night.key
            vote.voter = vote_data['voter']
            if vote_data['voter'] == current_user_person_name(): # Only allow person to vote for himself
                vote.present = vote_data.get('present')
                vote.appetizer = vote_data.get('appetizer')
                vote.main_course = vote_data.get('main_course')
                vote.dessert = vote_data.get('dessert')
                vote.game = vote_data.get('game')
            vote.put()

    game_night.put()
    game_night.calculate_and_save_sum()
    return game_night


app = webapp2.WSGIApplication([
    (r'/api/gamenights/', GameNightsHandler),
    (r'/api/gamenights/(\d+)/', GameNightHandler)
], debug=True)
