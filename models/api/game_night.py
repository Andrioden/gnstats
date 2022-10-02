from datetime import date
from typing import List

from pydantic import BaseModel

from models.api.vote import VoteCreate, VoteUpdate


class GameNightBase(BaseModel):
    host: str
    date: date
    description: str


class GameNightCreate(GameNightBase):
    votes: List[VoteCreate]


class GameNightUpdate(GameNightBase):
    votes: List[VoteUpdate]
