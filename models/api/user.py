from pydantic import BaseModel


class ClaimUserData(BaseModel):
    name: str
