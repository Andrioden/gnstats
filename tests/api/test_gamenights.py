from fastapi.testclient import TestClient
from google.cloud.ndb import Context
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from models.db.game_night import GameNight
from models.db.vote import Vote
from tests.data_service import DataService


def test_gamenights_api_post(clean_db_context: Context, client_as_activated: TestClient) -> None:
    response = client_as_activated.post(
        url="/api/gamenights/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "votes": [{"voter": DataService.create_person("Ole").name, "present": True}],
        },
    )
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert data["host"] == "Stian"


def test_gamenights_api_put(clean_db_context: Context, client_as_activated: TestClient) -> None:
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(game_night=game_night, voter="André", appetizer=1)

    # Test
    response = client_as_activated.put(
        url=f"/api/gamenights/{game_night.id}/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "votes": [
                {
                    "id": vote.id,
                    "voter": DataService.create_person("André").name,
                    "present": True,
                    "appetizer": 2,
                }
            ],
        },
    )
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert data["votes"][0]["voter"] == "André"
    assert data["votes"][0]["appetizer"] == 2


def test_gamenights_api_delete_as_admin(
    clean_db_context: Context, client_as_admin: TestClient
) -> None:
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(game_night)

    # Test
    response = client_as_admin.delete(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTP_200_OK
    assert GameNight.get_by_id(game_night.id) is None
    assert Vote.get_by_id(vote.id) is None


def test_gamenights_api_delete_as_anon(
    clean_db_context: Context, client_as_anon: TestClient
) -> None:
    game_night = DataService.create_game_night()

    response = client_as_anon.delete(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTP_401_UNAUTHORIZED


def test_gamenights_api_get_many(clean_db_context: Context, client_as_anon: TestClient) -> None:
    DataService.create_game_night()

    response = client_as_anon.get("/api/gamenights/")
    assert response.status_code == HTTP_200_OK
    assert len(response.json()) > 0


def test_gamenights_api_get_one(clean_db_context: Context, client_as_anon: TestClient) -> None:
    game_night = DataService.create_game_night()

    response = client_as_anon.get(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTP_200_OK
    assert response.json()["id"] == game_night.id
