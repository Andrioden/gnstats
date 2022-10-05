from typing import List, Optional

from fastapi import APIRouter, Depends

from models.api.user import ClaimPersonData, UpdatePersonData
from models.db.person import Person
from models.external.google import GoogleUser
from repos.person import PersonRepo

from .decorators import ensure_db_context
from .session import me_admin_or_401, me_user, me_user_or_401

router = APIRouter()


@router.post("/me/verify/")
@ensure_db_context
def post_me_verify(data: ClaimPersonData, user: GoogleUser = Depends(me_user_or_401)) -> None:
    if data.name not in Person.api_get_available_names():
        raise Exception("Name not available")
    PersonRepo.create(user=user, name=data.name)


@router.put("/{id_}/", dependencies=[Depends(me_admin_or_401)])
@ensure_db_context
def put(id_: int, data: UpdatePersonData) -> None:
    PersonRepo.update_activated(id_=id_, value=data.activated)


@router.get("/", response_model=List[dict])
@ensure_db_context
def get_many() -> List[dict]:
    return [person.get_data() for person in PersonRepo.get_all()]


@router.get("/available-names/", response_model=List[str])
@ensure_db_context
def get_available_names() -> List[str]:
    return Person.api_get_available_names()


@router.get("/me/", response_model=dict)
@ensure_db_context
def get_me(user: Optional[GoogleUser] = Depends(me_user)) -> dict:
    if user:
        person = PersonRepo.get_one_or_none_by_google_id(user.sub)
        return {
            "google_email": user.email,
            "name": person.name if person else None,
            "person": True if person else False,
            "admin": person.admin if person else False,
        }
    else:
        return {}
