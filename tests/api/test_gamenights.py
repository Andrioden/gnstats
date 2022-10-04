from http import HTTPStatus

from fastapi.testclient import TestClient

from api.app import app
from models.db.game_night import GameNight
from models.db.vote import Vote
from tests.data_service import DataService

client = TestClient(app)


def test_gamenights_api_post(clean_db_context) -> None:
    response = client.post(
        url="/api/gamenights/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "votes": [{"voter": DataService.ensure_person("Ole").name, "present": True}],
        },
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["host"] == "Stian"


def test_gamenights_api_put(clean_db_context) -> None:
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(game_night=game_night, voter="André", appetizer=1)

    # Test
    response = client.put(
        url=f"/api/gamenights/{game_night.id}/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "votes": [
                {
                    "id": vote.id,
                    "voter": DataService.ensure_person("André").name,
                    "present": True,
                    "appetizer": 2,
                }
            ],
        },
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["votes"][0]["voter"] == "André"
    assert data["votes"][0]["appetizer"] == 2


def test_gamenights_api_delete(clean_db_context) -> None:
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(game_night)

    # Test
    response = client.delete(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTPStatus.OK
    assert GameNight.get_by_id(game_night.id) is None
    assert Vote.get_by_id(vote.id) is None


def test_gamenights_api_get_many(clean_db_context) -> None:
    DataService.create_game_night()

    response = client.get("/api/gamenights/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) > 0


def test_gamenights_api_get_one(clean_db_context) -> None:
    game_night = DataService.create_game_night()

    response = client.get(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["id"] == game_night.id
