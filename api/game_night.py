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
        data = [game_night.get_data(current_user_person_name()) for game_night in GameNight.query()]
        set_json_response(self.response, data)

    @require_verified
    @require_request_data(['host', 'date', 'description'])
    def post(self):
        game_night = _create_or_update(self)
        if game_night is None:
            return
        else:
            set_json_response(self.response, {'response': "OK"})


class GameNightHandler(webapp2.RequestHandler):
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
    game_night.sum = 0

    if gn_id is None: # To get an ID for vote(s)
        game_night.put()

    vote_ids = []
    for vote_data in request_data['votes']:
        if vote_data['voter'] == request_data['host']:
            continue

        if not Person.query(Person.name == vote_data['voter']).get().activated:
            error(400, request_handler.response, "ERROR_INACTIVE_CANT_VOTE", "Deactivated person is not allowed to vote!")
            return None

        if vote_data.has_key('id'):
            vote_id = int(vote_data['id'])
            vote = Vote.get_by_id(vote_id)
            vote_ids.append(vote_id)
        else:
            vote = Vote()

        requesting_name = current_user_person_name()
        vote.game_night = game_night.key
        vote.voter = vote_data['voter']
        if vote_data['voter'] == current_user_person_name(): # Only allow person to vote for himself
            vote.appetizer = vote_data.get('appetizer')
            vote.main_course = vote_data.get('main_course')
            vote.dessert = vote_data.get('dessert')
            vote.game = vote_data.get('game')
        vote.put()

        game_night.sum += vote.weighed_sum()

    # The game night sum also has to have the sum added from the other votes
    for vote in Vote.query(Vote.game_night == game_night.key):
        if vote.key.id() not in vote_ids:
            game_night.sum += vote.weighed_sum()

    game_night.put()

    return game_night


app = webapp2.WSGIApplication([
    (r'/api/game_night/', GameNightsHandler),
    (r'/api/game_night/(\d+)/', GameNightHandler)
], debug=True)
