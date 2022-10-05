from typing import Optional

from fastapi import HTTPException
from starlette import status
from starlette.requests import Request

from api.decorators import ensure_db_context
from models.db.person import Person
from models.external.google import GoogleUser

SESSION_VAR_GOOGLE_USER = "GN_GOOGLE_USER"


def me_user(request: Request) -> Optional[GoogleUser]:
    if user_dict := request.session.get(SESSION_VAR_GOOGLE_USER):
        return GoogleUser.parse_obj(user_dict)
    else:
        return None


def me_user_or_401(request: Request) -> GoogleUser:
    if user := me_user(request):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a google account",
        )


@ensure_db_context
def me_person_or_401(request: Request) -> Person:
    user = me_user_or_401(request)
    if person := Person.query(Person.google_account_id == user.sub).get():
        return person
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a person",
        )
