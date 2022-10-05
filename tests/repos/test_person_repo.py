from google.cloud.ndb import Context

from repos.person import PersonRepo
from tests.data_service import DataService


def test_person_repo_get_one_or_none_by_name(clean_db_context: Context) -> None:
    DataService.ensure_person("Ole")

    assert PersonRepo.get_one_or_none_by_name("Ole") is not None
    assert PersonRepo.get_one_or_none_by_name("Stian") is None


def test_person_repo_get_all(clean_db_context: Context) -> None:
    assert len(PersonRepo.get_all()) == 0
    DataService.ensure_person("Ole")
    assert len(PersonRepo.get_all()) == 1
