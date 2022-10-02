#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
from typing import Optional, List

from fastapi import APIRouter, HTTPException, UploadFile, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import RedirectResponse

from models import *
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import RequestTooLargeError

from models.db.person import person_names_allowed
from .utils import *
from .decorators import *


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/oauth/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.get("/", response_model=List[dict])
@ensure_db_context
def get_many() -> List[dict]:
    return [person.get_data() for person in Person.query()]


@router.get("/available-names/", response_model=List[str])
@ensure_db_context
def get_available_names() -> List[str]:
    person_names_taken = [person.name for person in Person.query()]
    return [name for name in person_names_allowed if name not in person_names_taken]


@router.get("/me/", response_model=dict)
@ensure_db_context
def get_me() -> dict:
    user = users.get_current_user()
    if user:
        person = Person.query(Person.userid == user.user_id()).get()
        return {
            'name': person.name if person else None,
            'nickname': user.nickname(),
            'verified': True if person else False,
            'is_admin': users.is_current_user_admin()
        }
    else:
        return {}


@router.post("/me/avatar/")
@ensure_db_context
def post_me_avatar(file: UploadFile) -> None:
    try:
        person = me_person()
        person.avatar = file.file.read()
        person.put()
    except RequestTooLargeError:
        raise HTTPException(status_code=404, detail="File to large")


@router.get("/me/login/")
def get_me_login() -> RedirectResponse:
    return RedirectResponse(users.create_login_url("/", "gmail.com"))

# class MyLoginHandler(webapp2.RequestHandler):
#     def get(self):
#         redirect = self.request.get('redirect', "/")
#         return webapp2.redirect(users.create_login_url(redirect))
#
#
# class MyLogoutHandler(webapp2.RequestHandler):
#     def get(self):
#         redirect = self.request.get('redirect', "/")
#         return webapp2.redirect(users.create_logout_url(redirect))
#
#
# class MyVerifyHandler(webapp2.RequestHandler):
#     @require_request_data(['name', 'password'])
#     def post(self):
#         request_data = json.loads(self.request.body)
#
#         if not request_data['password'] == SitePassword:
#             error(400, self.response, "error_bad_password", "Bad password")
#             return
#
#         user = users.get_current_user()
#         Person(
#             name=request_data['name'],
#             userid=user.user_id(),
#             nickname=user.nickname()
#         ).put()
#
#         ok_204(self.response)
#
#
# class UserHandler(webapp2.RequestHandler):
#     @require_admin
#     def put(self, person_id):
#         request_data = json.loads(self.request.body)
#         person = Person.get_by_id(int(person_id))
#
#         if 'activated' in request_data:
#             person.activated = request_data['activated']
#
#         person.put()
#
#
# class UserAvatarHandler(webapp2.RequestHandler):
#     def get(self, person_id):
#         person = Person.get_by_id(int(person_id))
#         if person and person.avatar:
#             self.response.headers['Content-Type'] = 'image/jpeg'
#             self.response.cache_control = 'public'
#             self.response.cache_control.max_age = 300
#             self.response.out.write(person.avatar)
#         else:
#             self.abort(404)
#
#
# app = webapp2.WSGIApplication([
#     (r'/api/users/me/login/', MyLoginHandler),
#     (r'/api/users/me/logout/', MyLogoutHandler),
#     (r'/api/users/me/verify/', MyVerifyHandler),
#     (r'/api/users/(\d+)/', UserHandler),
#     (r'/api/users/(\d+)/avatar/', UserAvatarHandler),
# ], debug=True)
