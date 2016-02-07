import webapp2
import json
import logging
import time
from models import *
from google.appengine.api import users
from utils import *


class SyncHandler(webapp2.RequestHandler):
    def put(self):
        request_data = json.loads(self.request.body)
        logging.info(request_data)

        gn = GameNight(
            host=request_data['host'],
            date=time.strptime("request_data['date']", "%d.%m%.Y"),
        )


        set_json_response(self.response, {'user_name': "AndriodHardcoded"})


app = webapp2.WSGIApplication([
    (r'/api/game_night/sync', SyncHandler)
], debug=True)
