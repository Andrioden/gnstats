from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from google.cloud import ndb
from starlette import status

from fastapi import Request
from starlette.responses import RedirectResponse

import os
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

from api.decorators import ensure_db_context
from models.db.person import Person
from models.external.google import GoogleUser

router = APIRouter()

oauth = OAuth(Config(environ={'GOOGLE_CLIENT_ID': os.environ['GOOGLE_CLIENT_ID'],
                              'GOOGLE_CLIENT_SECRET': os.environ['GOOGLE_CLIENT_SECRET']}))
oauth_google_client = oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)


SESSION_VAR_GOOGLE_USER = "GN_GOOGLE_USER"


def get_person(google_account_id: str) -> Optional[Person]:
    return Person.query(Person.google_account_id == google_account_id).get()


def me_google_user(request: Request) -> Optional[GoogleUser]:
    if user_dict := request.session.get(SESSION_VAR_GOOGLE_USER):
        return GoogleUser.parse_obj(user_dict)
    else:
        return None

def me_google_user_or_401(request: Request) -> GoogleUser:
    if user := me_google_user(request):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a google account",
        )


@ensure_db_context
def me_person_or_401(request: Request) -> Person:
    user = me_google_user_or_401(request)
    if person := Person.query(Person.google_account_id == user.sub).get():
        return person
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a person",
        )


@router.get('/login/')
async def login(request: Request):
    redirect_uri = request.url_for('callback')
    return await oauth_google_client.authorize_redirect(request, redirect_uri)


@router.get('/callback/')
async def callback(request: Request):
    token = await oauth_google_client.authorize_access_token(request)
    google_user_info = GoogleUser.parse_obj(token["userinfo"])
    request.session[SESSION_VAR_GOOGLE_USER] = google_user_info.dict()
    return RedirectResponse(url='/')


@router.get('/logout/')
async def logout(request: Request):
    request.session.pop(SESSION_VAR_GOOGLE_USER, None)
    return RedirectResponse(url='/')


# @router.get('/test/person/', response_model=dict)
# def get_person(person: Person = Depends(me_person_or_401)) -> dict:
#     return person.get_data()
#
#
# @router.get('/test/google_user/', response_model=GoogleUser)
# def get_user(user: GoogleUser = Depends(me_google_user_or_401)):
#     return user
