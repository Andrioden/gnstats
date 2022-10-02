from http import HTTPStatus

from starlette.testclient import TestClient

from api.app import app
from api.decorators import ensure_db_context
from tests.data_service import DataService

client = TestClient(app)


@ensure_db_context
def test_users_api_get_many() -> None:
    DataService.ensure_person("André")

    response = client.get("/api/users/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) > 0


@ensure_db_context
def test_users_api_get_available_names() -> None:
    DataService.ensure_person_deleted("Ole")

    response = client.get("/api/users/available-names/")
    assert response.status_code == HTTPStatus.OK
    assert "Ole" in response.json()


def test_users_api_get_me() -> None:
    response = client.get("/api/users/me/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {}


def test_users_api_post_me_avatar() -> None:
    # _test_upload_file = Path('/usr/src/app/tests/files', 'new-index.json')
    _files = {'file': "./test_users.py"}
    with TestClient(app) as client_:
        response = client_.post('/api/users/me/avatar/', files=_files)
        assert response.status_code == HTTPStatus.OK

    # # remove the test file from the config directory
    # _copied_file = Path('/usr/src/app/config', 'new-index.json')
    # _copied_file.unlink()