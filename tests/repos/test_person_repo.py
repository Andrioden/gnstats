import pytest
from google.cloud.ndb import Context

from repos import IntegrityError, NotFoundError
from repos.person import PersonRepo
from tests.data_service import DataService


def test_person_repo_create(clean_db_context: Context) -> None:
    user = DataService.build_user()

    # Ok
    PersonRepo.create(user=user, name="Ole")

    # Not ok for same user to be connected to 2 persons
    with pytest.raises(IntegrityError):
        PersonRepo.create(user=user, name="Ole")


def test_person_repo_update_activated(clean_db_context: Context) -> None:
    person = DataService.create_person(name="Ole", activated=True)

    PersonRepo.update_activated(person.id, False)
    assert PersonRepo.get(person.id).activated is False

    PersonRepo.update_activated(person.id, True)
    assert PersonRepo.get(person.id).activated is True


def test_person_repo_get(clean_db_context: Context) -> None:
    person = DataService.create_person("Ole")

    assert PersonRepo.get(person.id) is not None

    with pytest.raises(NotFoundError):
        PersonRepo.get(-1)


def test_person_repo_get_one_or_none_by_name(clean_db_context: Context) -> None:
    DataService.create_person("Ole")

    assert PersonRepo.get_one_or_none_by_name("Ole") is not None
    assert PersonRepo.get_one_or_none_by_name("Stian") is None


def test_person_repo_get_all(clean_db_context: Context) -> None:
    assert len(PersonRepo.get_all()) == 0
    DataService.create_person("Ole")
    assert len(PersonRepo.get_all()) == 1
