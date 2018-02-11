#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import json
from google.appengine.ext import ndb
from models import *
from utils import *
from decorators import *
from pprint import pprint, pformat


class StatsHandler(webapp2.RequestHandler):
    def get(self):

        # First we cache a hierarky of the games and votes in a fast-accessing games id dict
        gn_votes = {}

        for gn in GameNight.query():
            gn._votes = []
            gn_votes[gn.key.id()] = gn

        for vote in Vote.query():
            gn_id = vote.game_night.id()
            if gn_id in gn_votes:
                gn_votes[gn_id]._votes.append(vote)
            else:
                logging.info("Game night %s not found", gn_id)

        behaviors = {}

        for gn_id, gn in gn_votes.iteritems():

            # Stats - Vote Behavior
            vote_count = len(gn._votes) * 1.0
            avg_vote = {
                'appetizer': sum([vote.appertizer_int() for vote in gn._votes]) / vote_count, 
                'main_course': sum([vote.main_course_int() for vote in gn._votes]) / vote_count,  
                'dessert': sum([vote.dessert_int() for vote in gn._votes]) / vote_count,  
                'game': sum([vote.game_int() for vote in gn._votes]) / vote_count, 
                'sum': sum([vote.nonweighed_sum() for vote in gn._votes]) / vote_count,
            }

            for vote in gn._votes:
                if vote.voter not in behaviors:
                    behaviors[vote.voter] = { 'count': 0, 'sum': 0, 'appetizer': 0, 'main_course': 0, 'dessert': 0, 'game': 0 }
                
                behaviors[vote.voter]['count'] += 1
                behaviors[vote.voter]['appetizer'] += vote.appertizer_int() - avg_vote['appetizer']
                behaviors[vote.voter]['main_course'] += vote.main_course_int() - avg_vote['main_course']
                behaviors[vote.voter]['dessert'] += vote.dessert_int() - avg_vote['dessert']
                behaviors[vote.voter]['game'] += vote.game_int() - avg_vote['game']
                behaviors[vote.voter]['sum'] += vote.nonweighed_sum() - avg_vote['sum']
        
        # Convert to array as its better for the client
        behaviors_arr = []
        for person, behavior in behaviors.iteritems():
            behavior['person'] = person
            behavior['appetizer'] = behavior['appetizer'] / behavior['count']
            behavior['main_course'] = behavior['main_course'] / behavior['count']
            behavior['dessert'] = behavior['dessert'] / behavior['count']
            behavior['game'] = behavior['game'] / behavior['count']
            behavior['sum'] = behavior['sum'] / behavior['count']
            behaviors_arr.append(behavior)

        set_json_response(self.response, {'behaviors': behaviors_arr})


app = webapp2.WSGIApplication([
    (r'/api/actions/stats/', StatsHandler),
], debug=True)