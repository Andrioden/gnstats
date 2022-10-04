#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import RequestTooLargeError
from pydantic import BaseModel
from starlette.responses import RedirectResponse

from models import *
from models.api.user import ClaimUserData
from models.db.person import person_names_allowed
from models.external.google import GoogleUser

from .auth import me_google_user, me_google_user_or_401
from .decorators import *
from .utils import *

router = APIRouter()


@router.get("/", response_model=List[dict])
@ensure_db_context
def get_many() -> List[dict]:
    return [person.get_data() for person in Person.query()]


@router.get("/available-names/", response_model=List[str])
@ensure_db_context
def get_available_names() -> List[str]:
    return Person.api_get_available_names()


@router.get("/me/", response_model=dict)
@ensure_db_context
def get_me(user: Optional[GoogleUser] = Depends(me_google_user)) -> dict:
    if user:
        person = Person.query(Person.google_account_id == user.sub).get()
        return {
            "google_email": user.email,
            "name": person.name if person else None,
            "person": True if person else False,
            "admin": person.admin if person else False,
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


@router.post("/me/claim/")
@ensure_db_context
def post_me_claim(data: ClaimUserData, user: GoogleUser = Depends(me_google_user_or_401)) -> None:
    if data.name not in Person.api_get_available_names():
        raise Exception("Name not available")

    Person(
        google_account_id=user.sub,
        google_email=user.email,
        google_picture_url=user.picture,
        name=data.name,
    ).put()


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
#     (r'/api/users/(\d+)/', UserHandler),
#     (r'/api/users/(\d+)/avatar/', UserAvatarHandler),
# ], debug=True)
