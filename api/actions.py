#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import json
# from google.cloud import ndb
# from models import *
# from .utils import *
# from .decorators import *
# from pprint import pprint, pformat


# class StatsHandler(webapp2.RequestHandler):
#     def get(self):
#
#         # First we cache a hierarchy of the games and votes in a fast-accessing games id dict
#         gn_votes = {}
#
#         for gn in GameNight.query():
#             gn._votes = []
#             gn_votes[gn.key.id()] = gn
#
#         for vote in Vote.query(Vote.present == True):
#             gn_id = vote.game_night.id()
#             if gn_id in gn_votes:
#                 gn_votes[gn_id]._votes.append(vote)
#             else:
#                 logging.info("Game night %s not found", gn_id)
#
#         # Convert dict to array for easier further processing:
#         gn_votes_arr = []
#         for gn_id, gn in gn_votes.items():
#             gn_votes_arr.append(gn)
#
#         # Calculate stats
#         stats_data = {
#             'behaviors': self._behaviors(gn_votes_arr),
#             'host_performances': self._host_performances(gn_votes_arr)
#         }
#
#         # Response
#         ok_200(self.response, stats_data)
#
#     def _behaviors(self, gn_votes):
#
#         behaviors = {}
#
#         for gn in gn_votes:
#
#             vote_count = len(gn._votes) * 1.0
#             avg_vote = {
#                 'appetizer': sum([vote.appertizer_int() for vote in gn._votes]) / vote_count,
#                 'main_course': sum([vote.main_course_int() for vote in gn._votes]) / vote_count,
#                 'dessert': sum([vote.dessert_int() for vote in gn._votes]) / vote_count,
#                 'game': sum([vote.game_int() for vote in gn._votes]) / vote_count,
#                 'sum': sum([vote.nonweighed_sum() for vote in gn._votes]) / vote_count,
#                 'sum_weighed': sum([vote.weighed_sum() for vote in gn._votes]) / vote_count,
#             }
#
#             for vote in gn._votes:
#                 if vote.voter not in behaviors:
#                     behaviors[vote.voter] = { 'count': 0, 'appetizer': 0, 'main_course': 0, 'dessert': 0, 'game': 0, 'sum': 0, 'sum_weighed': 0 }
#
#                 behaviors[vote.voter]['count'] += 1
#                 behaviors[vote.voter]['appetizer'] += vote.appertizer_int() - avg_vote['appetizer']
#                 behaviors[vote.voter]['main_course'] += vote.main_course_int() - avg_vote['main_course']
#                 behaviors[vote.voter]['dessert'] += vote.dessert_int() - avg_vote['dessert']
#                 behaviors[vote.voter]['game'] += vote.game_int() - avg_vote['game']
#                 behaviors[vote.voter]['sum'] += vote.nonweighed_sum() - avg_vote['sum']
#                 behaviors[vote.voter]['sum_weighed'] += vote.weighed_sum() - avg_vote['sum_weighed']
#
#         # Convert to array as its better for the client
#         behaviors_arr = []
#         for person, behavior in behaviors.items():
#             behavior['person'] = person
#             behavior['appetizer'] = behavior['appetizer'] / behavior['count']
#             behavior['main_course'] = behavior['main_course'] / behavior['count']
#             behavior['dessert'] = behavior['dessert'] / behavior['count']
#             behavior['game'] = behavior['game'] / behavior['count']
#             behavior['sum'] = behavior['sum'] / behavior['count']
#             behavior['sum_weighed'] = behavior['sum_weighed'] / behavior['count']
#             behaviors_arr.append(behavior)
#
#         return behaviors_arr
#
#     def _host_performances(self, gn_votes):
#
#         host_performances = {
#             'total': {},
#             # In addition to one dict entry for each year
#         }
#
#         current_round_hosts_left = 0
#         current_round_year = None
#         current_round_best_sum = None
#         current_round_best_host = None
#         current_round_worst_sum = None
#         current_round_worst_host = None
#
#         for gn in sorted(gn_votes, key=lambda gn: gn.date):
#
#             # Initiate data structures if they are missing for new persons and new years
#             if not gn.host in host_performances['total']:
#                 host_performances['total'][gn.host] = { 'hosted': 0, 'best': 0, 'worst': 0, 'total_sum': 0, 'avg': None }
#
#             if not gn.date.year in host_performances:
#                 host_performances[gn.date.year] = {}
#
#             if not gn.host in host_performances[gn.date.year]:
#                 host_performances[gn.date.year][gn.host] = { 'hosted': 0, 'best': 0, 'worst': 0, 'total_sum': 0, 'avg': None }
#
#             # Store general stats
#             host_performances['total'][gn.host]['hosted'] += 1
#             host_performances['total'][gn.host]['total_sum'] += gn.sum
#             host_performances[gn.date.year][gn.host]['hosted'] += 1
#             host_performances[gn.date.year][gn.host]['total_sum'] += gn.sum
#
#             # Store and calculate best/worst stats
#             if current_round_hosts_left == 0:
#                 # New round started, add previous round data to dataset if not first round
#                 if current_round_best_host is not None:
#                     host_performances['total'][current_round_best_host]['best'] += 1
#                     host_performances['total'][current_round_worst_host]['worst'] += 1
#                     host_performances[current_round_year][current_round_best_host]['best'] += 1
#                     host_performances[current_round_year][current_round_worst_host]['worst'] += 1
#                 # Reset best/worst tracking variables
#                 current_round_hosts_left = len(gn._votes) + 1
#                 current_round_year = gn.date.year
#                 current_round_best_sum = -9999
#                 current_round_best_host = None
#                 current_round_worst_sum = 9999
#                 current_round_worst_host = None
#
#             if gn.sum > current_round_best_sum:
#                 current_round_best_sum = gn.sum
#                 current_round_best_host = gn.host
#
#             if gn.sum < current_round_worst_sum:
#                 current_round_worst_sum = gn.sum
#                 current_round_worst_host = gn.host
#
#             current_round_hosts_left -= 1
#
#         # Calculate averages
#         for year_or_tot, performances in host_performances.items():
#             for name, performance in performances.items():
#                 performance['avg'] = performance['total_sum'] / performance['hosted']
#
#         return host_performances
#
#
# app = webapp2.WSGIApplication([
#     (r'/api/actions/stats/', StatsHandler),
# ], debug=True)