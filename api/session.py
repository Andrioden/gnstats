from typing import Optional

from fastapi import Depends, HTTPException
from starlette import status
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

from models.db.user import User
from models.external.google import GoogleAccount
from repos.user import UserRepo
from utils.db import ensure_db_context

SESSION_VAR_GOOGLE_ACCOUNT = "GN_GOOGLE_ACCOUNT"


def me_google_acc_or_none(request: Request) -> Optional[GoogleAccount]:
    if google_acc_dict := request.session.get(SESSION_VAR_GOOGLE_ACCOUNT):
        return GoogleAccount.parse_obj(google_acc_dict)
    else:
        return None


def me_google_acc_or_401(request: Request) -> GoogleAccount:
    if google_acc := me_google_acc_or_none(request):
        return google_acc
    else:
        raise HTTPException(HTTP_401_UNAUTHORIZED, "Not logged into a google account")


@ensure_db_context
def me_or_none(
    google_acc: Optional[GoogleAccount] = Depends(me_google_acc_or_none),
) -> Optional[User]:
    if google_acc:
        return UserRepo.get_one_or_none_by_google_id(google_acc.sub)
    else:
        return None


@ensure_db_context
def me_or_401(google_acc: GoogleAccount = Depends(me_google_acc_or_401)) -> User:
    if user := UserRepo.get_one_or_none_by_google_id(google_acc.sub):
        return user
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Not logged into a user")


def me_activated_or_401(user: User = Depends(me_or_401)) -> User:
    if user.activated:
        return user
    else:
        raise HTTPException(HTTP_401_UNAUTHORIZED, "Not activated")


def me_admin_or_401(user: User = Depends(me_or_401)) -> User:
    if user.admin:
        return user
    else:
        raise HTTPException(HTTP_401_UNAUTHORIZED, "Not admin")
