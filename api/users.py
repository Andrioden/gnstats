from typing import List, Optional

from fastapi import APIRouter, Depends

from models.api.user import ClaimUserData, UpdateUserData
from models.external.google import GoogleAccount
from repos.user import UserRepo
from utils.db import ensure_db_context

from .session import me_admin_or_401, me_google_acc_or_401, me_google_acc_or_none

router = APIRouter()


@router.post("/me/verify/")
@ensure_db_context
def post_me_verify(
    data: ClaimUserData, google_acc: GoogleAccount = Depends(me_google_acc_or_401)
) -> None:
    if data.name not in UserRepo.get_available_names():
        raise Exception("Name not available")
    UserRepo.create(google_acc=google_acc, name=data.name)


@router.put("/{id_}/", dependencies=[Depends(me_admin_or_401)])
@ensure_db_context
def put(id_: int, data: UpdateUserData) -> None:
    UserRepo.update_activated(id_=id_, value=data.activated)


@router.get("/")
@ensure_db_context
def get_many() -> List[dict]:
    return [user.get_data() for user in UserRepo.get_all()]


@router.get("/available-names/")
@ensure_db_context
def get_available_names() -> List[str]:
    return UserRepo.get_available_names()


@router.get("/me/")
@ensure_db_context
def get_me(google_acc: Optional[GoogleAccount] = Depends(me_google_acc_or_none)) -> dict:
    if google_acc:
        user = UserRepo.get_one_or_none_by_google_id(google_acc.sub)
        return {
            "google_email": google_acc.email,
            "registered": True if user else False,
            "name": user.name if user else None,
            "admin": user.admin if user else False,
        }
    else:
        return {}
