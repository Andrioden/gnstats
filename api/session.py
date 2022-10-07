from typing import Optional

from fastapi import Depends, HTTPException
from starlette import status
from starlette.requests import Request

from api.utils import ensure_db_context
from models.db.person import Person
from models.external.google import GoogleUser
from repos.person import PersonRepo

SESSION_VAR_GOOGLE_USER = "GN_GOOGLE_USER"


def me_user_or_none(request: Request) -> Optional[GoogleUser]:
    if user_dict := request.session.get(SESSION_VAR_GOOGLE_USER):
        return GoogleUser.parse_obj(user_dict)
    else:
        return None


def me_user_or_401(request: Request) -> GoogleUser:
    if user := me_user_or_none(request):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a google account",
        )


@ensure_db_context
def me_or_none(user: Optional[GoogleUser] = Depends(me_user_or_none)) -> Optional[Person]:
    if user:
        return PersonRepo.get_one_or_none_by_google_id(user.sub)
    else:
        return None


@ensure_db_context
def me_or_401(user: GoogleUser = Depends(me_user_or_401)) -> Person:
    if person := PersonRepo.get_one_or_none_by_google_id(user.sub):
        return person
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged into a person",
        )


def me_activated_or_401(person: Person = Depends(me_or_401)) -> Person:
    if person.activated:
        return person
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not activated")


def me_admin_or_401(person: Person = Depends(me_or_401)) -> Person:
    if person.admin:
        return person
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not admin")
