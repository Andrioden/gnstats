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
        data = [game_night.get_data(current_user_person_name()) for game_night in GameNight.query()]
        set_json_response(self.response, data)

    def post(self):
        game_night = _create_or_update(self)
        if game_night is None:
            return
        else:
            set_json_response(self.response, {'response': "OK"})


class GameNightHandler(webapp2.RequestHandler):
    def put(self, gn_id):
        game_night = _create_or_update(self, gn_id)
        if game_night is None:
            return
        else:
            set_json_response(self.response, {'response': "OK"})

    def delete(self, gn_id):
        if not validate_logged_in_admin(self.response):
            return

        gn_key = GameNight.get_by_id(int(gn_id)).key
        ndb.delete_multi(Vote.query(Vote.game_night == gn_key).fetch(keys_only=True))
        gn_key.delete()

        set_json_response(self.response, {'response': "OK"})


def _create_or_update(request_obj, gn_id = None):
    if not validate_authenticated(request_obj.response):
        return None

    request_data = json.loads(request_obj.request.body)
    logging.info(request_data)

    if not validate_request_data(request_obj.response, request_data, ['host', 'date', 'description']):
        return None

    # Create/Update GameNight
    if gn_id is not None:
        game_night = GameNight.get_by_id(int(gn_id))
    else:
        game_night = GameNight()

    game_night.date = datetime.strptime(request_data['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
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
            error_400(request_obj.response, "ERROR_INACTIVE_CANT_VOTE", "Deactivated person is not allowed to vote!")
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
