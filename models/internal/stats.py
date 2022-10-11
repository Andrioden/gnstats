from pydantic import BaseModel


class Behaviour(BaseModel):
    user: str
    count: int = 0
    appetizer: float = 0
    main_course: float = 0
    dessert: float = 0
    game: float = 0
    sum: float = 0
    sum_weighed: float = 0


class HostPerformance(BaseModel):
    hosted: int = 0
    total_sum: int = 0
    avg: float = 0.0
