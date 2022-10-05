from typing import Optional

from fastapi import Depends, HTTPException
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
def me_person_or_401(user: GoogleUser = Depends(me_user_or_401)) -> Person:
    if person := Person.query(Person.google_id == user.sub).get():
        return person
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a person",
        )


def me_activated_or_401(person: Person = Depends(me_person_or_401)) -> None:
    if not person.activated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not activated")


def me_admin_or_401(person: Person = Depends(me_person_or_401)) -> None:
    if not person.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not admin")
