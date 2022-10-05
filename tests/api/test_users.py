from http import HTTPStatus

from google.cloud.ndb import Context
from starlette.testclient import TestClient

from api.app import app
from tests.data_service import DataService

client = TestClient(app)


def test_users_api_get_many(clean_db_context: Context) -> None:
    DataService.ensure_person("André")

    response = client.get("/api/users/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) > 0


def test_users_api_get_available_names(clean_db_context: Context) -> None:
    response = client.get("/api/users/available-names/")
    assert response.status_code == HTTPStatus.OK
    assert "Ole" in response.json()


def test_users_api_get_me_empty() -> None:
    response = client.get("/api/users/me/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {}


# def test_users_api_post_me_avatar() -> None:
#     with TestClient(app) as client_:
#         response = client_.post("/api/users/me/avatar/", files={"file": "./test_users.py"})
#         assert response.status_code == HTTPStatus.OK
