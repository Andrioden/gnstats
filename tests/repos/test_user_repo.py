import pytest
from google.cloud.ndb import Context

from repos import IntegrityError, NotFoundError
from repos.user import UserRepo
from tests.data_service import DataService


def test_user_repo_create(clean_db_context: Context) -> None:
    google_acc = DataService.build_google_account()

    # Ok
    UserRepo.create(google_acc=google_acc, name="Ole")

    # Not ok for 1 google account to be connected to 2 users
    with pytest.raises(IntegrityError):
        UserRepo.create(google_acc=google_acc, name="Ole")


def test_user_repo_update_activated(clean_db_context: Context) -> None:
    user = DataService.create_user(name="Ole", activated=True)

    UserRepo.update_activated(user.id, False)
    assert UserRepo.get(user.id).activated is False

    UserRepo.update_activated(user.id, True)
    assert UserRepo.get(user.id).activated is True


def test_user_repo_exists(clean_db_context: Context) -> None:
    DataService.create_user(name="Stian", activated=True)
    DataService.create_user(name="André", activated=False)

    assert UserRepo.exists(name="Stian", activated=True) is True
    assert UserRepo.exists(name="Stian", activated=False) is False

    assert UserRepo.exists(name="André", activated=True) is False
    assert UserRepo.exists(name="André", activated=False) is True

    assert UserRepo.exists(name="Ole", activated=True) is False
    assert UserRepo.exists(name="Ole", activated=False) is False


def test_user_repo_get(clean_db_context: Context) -> None:
    user = DataService.create_user("Ole")

    assert UserRepo.get(user.id) is not None

    with pytest.raises(NotFoundError):
        UserRepo.get(-1)


def test_user_repo_get_one_or_none_by_name(clean_db_context: Context) -> None:
    DataService.create_user("Ole")

    assert UserRepo.get_one_or_none_by_name("Ole") is not None
    assert UserRepo.get_one_or_none_by_name("Stian") is None


def test_user_repo_get_all(clean_db_context: Context) -> None:
    assert len(UserRepo.get_all()) == 0
    DataService.create_user("Ole")
    assert len(UserRepo.get_all()) == 1


def test_user_repo_get_available_names(clean_db_context: Context) -> None:
    assert "Ole" in UserRepo.get_available_names()
    DataService.create_user("Ole")
    assert "Ole" not in UserRepo.get_available_names()
