import pytest

from repos import NotFoundError
from repos.vote import VoteRepo
from tests.data_service import DataService


def test_vote_repo_count_all(clean_db_context) -> None:
    assert VoteRepo.count_all() == 0
    DataService.create_vote()
    assert VoteRepo.count_all() == 1


def test_vote_repo_get(clean_db_context):
    vote = DataService.create_vote()

    assert VoteRepo.get(vote.id) is not None

    with pytest.raises(NotFoundError):
        VoteRepo.get(-1)


def test_vote_repo_get_many_by_present(clean_db_context):
    game_night = DataService.create_game_night()

    DataService.create_vote(game_night=game_night, present=True)
    assert len(VoteRepo.get_many_by_present(game_night)) == 1

    DataService.create_vote(game_night=game_night, present=False)
    assert len(VoteRepo.get_many_by_present(game_night)) == 1
