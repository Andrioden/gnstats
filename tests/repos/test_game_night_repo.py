import pytest

from repos import NotFoundError
from repos.game_night import GameNightRepo
from repos.vote import VoteRepo
from tests.data_service import DataService


def test_game_night_repo_delete_by_id(clean_db_context) -> None:
    # Dont delete these
    game_night1 = DataService.create_game_night()
    DataService.create_vote(game_night1)
    DataService.create_vote(game_night1)

    # Delete these
    game_night2 = DataService.create_game_night()
    DataService.create_vote(game_night2)

    # Test
    assert GameNightRepo.count_all() == 2
    assert VoteRepo.count_all() == 3

    GameNightRepo.delete_by_id(game_night1.id)
    assert GameNightRepo.count_all() == 1
    assert VoteRepo.count_all() == 1

    GameNightRepo.delete_by_id(game_night2.id)
    assert GameNightRepo.count_all() == 0
    assert VoteRepo.count_all() == 0


def test_game_night_repo_count_all(clean_db_context) -> None:
    assert GameNightRepo.count_all() == 0
    DataService.create_game_night()
    assert GameNightRepo.count_all() == 1


def test_game_night_repo_get(clean_db_context):
    game_night = DataService.create_game_night()

    assert GameNightRepo.get(game_night.id) is not None

    with pytest.raises(NotFoundError):
        GameNightRepo.get(-1)