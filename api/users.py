from typing import List, Optional

from fastapi import APIRouter, Depends

from models.api.user import ClaimUserData
from models.db.person import Person
from models.external.google import GoogleUser
from repos.person import PersonRepo

from .decorators import ensure_db_context
from .session import me_user, me_user_or_401

router = APIRouter()


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
        person = Person.query(Person.google_account_id == user.sub).get()
        return {
            "google_email": user.email,
            "name": person.name if person else None,
            "person": True if person else False,
            "admin": person.admin if person else False,
        }
    else:
        return {}


# @router.post("/me/avatar/")
# @ensure_db_context
# def post_me_avatar(file: UploadFile) -> None:
#     try:
#         person = me_person()
#         person.avatar = file.file.read()  # type: ignore
#         person.put()  # type: ignore
#     except RequestTooLargeError:
#         raise HTTPException(status_code=404, detail="File to large")


@router.post("/me/claim/")
@ensure_db_context
def post_me_claim(data: ClaimUserData, user: GoogleUser = Depends(me_user_or_401)) -> None:
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
