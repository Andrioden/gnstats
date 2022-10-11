from datetime import datetime

from google.cloud.ndb import Context

from tests.data_service import DataService
from utils.stats_calculator import StatsCalculator


def test_stats_calculator_behaviour(clean_db_context: Context) -> None:
    # Setup
    game_night = DataService.build_game_night(id_=1)
    calc = StatsCalculator(
        game_nights=[game_night],
        votes=[
            DataService.build_vote(game_night, voter="André", game=1),
            DataService.build_vote(game_night, voter="Ole", game=6),
        ],
    )

    # Test
    behaviors = calc.behaviors()
    assert len(behaviors) == 2

    assert behaviors[0].user == "André"
    assert behaviors[0].count == 1
    assert behaviors[0].appetizer == 0
    assert behaviors[0].main_course == 0
    assert behaviors[0].dessert == 0
    assert behaviors[0].game == -2.5  # 2.5 under average, which is (1+6 / 2 = 3.5)
    assert behaviors[0].sum == -2.5
    assert behaviors[0].sum_weighed == -1.25  # Game is weighed as 0.5

    assert behaviors[1].user == "Ole"
    assert behaviors[1].count == 1
    assert behaviors[1].appetizer == 0
    assert behaviors[1].main_course == 0
    assert behaviors[1].dessert == 0
    assert behaviors[1].game == 2.5
    assert behaviors[1].sum == 2.5
    assert behaviors[1].sum_weighed == 1.25


def test_stats_calculator_host_performances(clean_db_context: Context) -> None:
    # Setup
    gn1 = DataService.build_game_night(id_=1, host="André", sum_=1)
    gn2 = DataService.build_game_night(id_=2, host="Ole", sum_=2)
    calc = StatsCalculator(
        game_nights=[gn1, gn2],
        votes=[
            DataService.build_vote(gn1, voter="Ole"),
            DataService.build_vote(gn2, voter="André"),
        ],
    )

    # Test
    performances = calc.host_performances()

    assert performances["total"]["André"].hosted == 1
    assert performances["total"]["André"].total_sum == 1
    assert performances["total"]["André"].avg == 1
    assert performances["total"]["André"] == performances[datetime.now().year]["André"]

    assert performances["total"]["Ole"].hosted == 1
    assert performances["total"]["Ole"].total_sum == 2
    assert performances["total"]["Ole"].avg == 2
    assert performances["total"]["Ole"] == performances[datetime.now().year]["Ole"]


# def test_stats_calculator_host_performances_workbench(db_context: Context) -> None:
#     from repos.game_night import GameNightRepo
#     from repos.vote import VoteRepo
#
#     calc = StatsCalculator(
#         game_nights=GameNightRepo.get_all_with_sum(),
#         votes=VoteRepo.get_all_present(),
#     )
#     behaviors = calc.behaviors()
#     host_performances = calc.host_performances()
#     print(behaviors)
