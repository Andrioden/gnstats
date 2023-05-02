from fastapi import APIRouter

from repos.game_night import GameNightRepo
from repos.vote import VoteRepo
from utils.db import ensure_db_context
from utils.stats_calculator import StatsCalculator

router = APIRouter()


@router.get("/")
@ensure_db_context
def get() -> dict:
    stats_calculator = StatsCalculator(
        game_nights=GameNightRepo.get_all_with_sum(),
        votes=VoteRepo.get_all_present(),
    )
    return {
        "behaviors": stats_calculator.behaviors(),
        "host_performances": stats_calculator.host_performances(),
    }
