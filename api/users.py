import webapp2
import json
import logging
from models import *
from google.appengine.api import users
from utils import *
from config_hidden import SitePassword


class UserHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        user = users.get_current_user()
        if user:
            person = Person.query(Person.userid == user.user_id()).get()
            verified = True if person else False
            name = person.name if person else None
            set_json_response(self.response, {'name': name, 'nickname': user.nickname(), 'verified': verified, 'is_admin': users.is_current_user_admin()})
        else:
            set_json_response(self.response, {})


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        redirect = self.request.get('redirect', "/")
        return webapp2.redirect(users.create_login_url(redirect))


class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        redirect = self.request.get('redirect', "/")
        return webapp2.redirect(users.create_logout_url(redirect))


class VerifyHandler(webapp2.RequestHandler):
    def post(self):
        request_data = json.loads(self.request.body)

        if not validate_request_data(self.response, request_data, ['name', 'nickname', 'password']):
            return
        if not request_data['password'] == SitePassword:
            error_400(self.response, "error_bad_password", "Bad password")
            return

        user = users.get_current_user()
        Person(
            name=request_data['name'],
            userid=user.user_id(),
            nickname=user.nickname()
        ).put()

        set_json_response(self.response, {'response': "OK"})



app = webapp2.WSGIApplication([
    (r'/api/users/me/', UserHandler),
    (r'/api/users/login/', LoginHandler),
    (r'/api/users/logout/', LogoutHandler),
    (r'/api/users/verify/', VerifyHandler)
], debug=True)
