from pydantic import BaseModel


class ClaimUserData(BaseModel):
    name: str


class UpdateUserData(BaseModel):
    activated: bool
