from typing import Optional

from authlib.integrations.starlette_client import StarletteOAuth2App
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from starlette.responses import RedirectResponse

from api.decorators import ensure_db_context
from clients.oauth import google_oauth_client
from models.db.person import Person
from models.external.google import GoogleUser

router = APIRouter()


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


@router.get("/login/")
async def login(request: Request, oauth_client: StarletteOAuth2App = Depends(google_oauth_client)) -> RedirectResponse:
    redirect_uri = request.url_for("callback")
    return await oauth_client.authorize_redirect(request, redirect_uri)


@router.get("/callback/")
async def callback(
    request: Request,
    oauth_client: StarletteOAuth2App = Depends(google_oauth_client),
) -> RedirectResponse:
    token = await oauth_client.authorize_access_token(request)
    request.session[SESSION_VAR_GOOGLE_USER] = GoogleUser.parse_obj(token["userinfo"]).dict()
    return RedirectResponse(url="/")


@router.get("/logout/")
async def logout(request: Request) -> RedirectResponse:
    request.session.pop(SESSION_VAR_GOOGLE_USER, None)
    return RedirectResponse(url="/")


# @router.get('/test/person/', response_model=dict)
# def get_person(person: Person = Depends(me_person_or_401)) -> dict:
#     return person.get_data()
#
#
# @router.get('/test/google_user/', response_model=GoogleUser)
# def get_user(user: GoogleUser = Depends(me_google_user_or_401)):
#     return user
