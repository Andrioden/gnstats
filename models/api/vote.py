from typing import Optional

from pydantic import BaseModel


class VoteBase(BaseModel):
    voter: str
    present: bool
    appetizer: Optional[int]
    main_course: Optional[int]
    dessert: Optional[int]
    game: Optional[int]


class VoteCreate(VoteBase):
    pass


class VoteUpdate(VoteBase):
    id: int
