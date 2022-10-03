from pydantic import BaseModel


class GoogleUser(BaseModel):
    sub: str  # id
    email: str
    email_verified: bool
    picture: str
    name: str
