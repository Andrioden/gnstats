from http import HTTPStatus

from fastapi.testclient import TestClient

from api.app import app
from api.decorators import ensure_db_context
from models.db.game_night import GameNight
from models.db.vote import Vote
from tests.data_service import DataService

client = TestClient(app)


@ensure_db_context
def test_gamenights_api_post():
    response = client.post(
        url="/api/gamenights/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "votes": [
                {
                    "voter": DataService.ensure_person("Ole").name,
                    "present": True
                }
            ]
        }
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["host"] == "Stian"


@ensure_db_context
def test_gamenights_api_put():
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(
        game_night=game_night,
        voter="André",
        appetizer=1
    )

    # Test
    response = client.put(
        url=f"/api/gamenights/{game_night.key.id()}/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "votes": [
                {
                    "id": vote.key.id(),
                    "voter": DataService.ensure_person("André").name,
                    "present": True,
                    "appetizer": 2
                }
            ]
        }
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["votes"][0]["voter"] == "André"
    assert data["votes"][0]["appetizer"] == 2


@ensure_db_context
def test_gamenights_api_delete():
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(game_night)

    # Test
    response = client.delete(f"/api/gamenights/{game_night.key.id()}/")
    assert response.status_code == HTTPStatus.OK
    assert GameNight.get_by_id(game_night.key.id()) is None
    assert Vote.get_by_id(vote.key.id()) is None


@ensure_db_context
def test_gamenights_api_get_many():
    DataService.create_game_night()

    response = client.get("/api/gamenights/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) > 0


@ensure_db_context
def test_gamenights_api_get_one():
    game_night = DataService.create_game_night()

    response = client.get(f"/api/gamenights/{game_night.key.id()}/")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["id"] == game_night.key.id()
