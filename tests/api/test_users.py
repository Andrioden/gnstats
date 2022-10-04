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


def test_users_api_get_me_empty() -> None:
    response = client.get("/api/users/me/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {}


def test_users_api_post_me_avatar() -> None:
    with TestClient(app) as client_:
        response = client_.post("/api/users/me/avatar/", files={"file": "./test_users.py"})
        assert response.status_code == HTTPStatus.OK
