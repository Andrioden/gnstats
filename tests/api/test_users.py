from google.cloud.ndb import Context
from starlette.status import HTTP_200_OK
from starlette.testclient import TestClient

from tests.data_service import DataService


def test_users_api_get_many(clean_db_context: Context, client_as_anon: TestClient) -> None:
    DataService.create_user("André")

    response = client_as_anon.get("/api/users/")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) > 0


def test_users_api_get_available_names(
    clean_db_context: Context, client_as_anon: TestClient
) -> None:
    DataService.create_user("Stian")

    response = client_as_anon.get("/api/users/available-names/")
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert "Ole" in data
    assert "Stian" not in data


def test_users_api_get_me_as_anon(client_as_anon: TestClient) -> None:
    response = client_as_anon.get("/api/users/me/")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {}
