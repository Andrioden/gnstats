from pydantic import BaseModel


class ClaimPersonData(BaseModel):
    name: str


class UpdatePersonData(BaseModel):
    activated: bool
