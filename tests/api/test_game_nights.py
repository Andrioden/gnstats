from fastapi.testclient import TestClient
from google.cloud.ndb import Context
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from models.db.user import User
from repos.game_night import GameNightRepo
from repos.vote import VoteRepo
from tests.data_service import DataService


def test_game_nights_api_post(
    clean_db_context: Context,
    client_as_activated: TestClient,
    me_created: User,
) -> None:
    response = client_as_activated.post(
        url="/api/gamenights/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "round_start": False,
            "votes": [{"voter": me_created.name, "present": True}],
        },
    )
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert data["host"] == "Stian"


def test_game_nights_api_post_as_deactivated(
    clean_db_context: Context, client_as_deactivated: TestClient
) -> None:
    response = client_as_deactivated.post(url="/api/gamenights/")
    assert response.status_code == HTTP_401_UNAUTHORIZED


def test_game_nights_api_put(
    clean_db_context: Context,
    client_as_activated: TestClient,
    me_created: User,
) -> None:
    # A not completed game night vote
    game_night = DataService.create_game_night(sum_=None)
    vote = DataService.create_vote(game_night=game_night, voter=me_created.name, appetizer=None)

    # Test
    response = client_as_activated.put(
        url=f"/api/gamenights/{game_night.id}/",
        json={
            "host": "Stian",
            "date": "2020-01-01",
            "description": "test",
            "round_start": False,
            "votes": [
                {
                    "id": vote.id,
                    "voter": me_created.name,
                    "present": True,
                    "appetizer": 2,
                    "main_course": 2,
                    "dessert": 2,
                    "game": 2,
                }
            ],
        },
    )
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert data["votes"][0]["voter"] == me_created.name
    assert data["votes"][0]["appetizer"] == 2

    assert GameNightRepo.get(game_night.id).sum is not None


def test_game_nights_api_put_as_deactivated(
    clean_db_context: Context, client_as_deactivated: TestClient
) -> None:
    response = client_as_deactivated.put(url="/api/gamenights/1/")
    assert response.status_code == HTTP_401_UNAUTHORIZED


def test_game_nights_api_delete_as_admin(
    clean_db_context: Context, client_as_admin: TestClient
) -> None:
    # Setup
    game_night = DataService.create_game_night()
    vote = DataService.create_vote(game_night)

    # Test
    response = client_as_admin.delete(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTP_200_OK
    assert GameNightRepo.get_one_or_none(game_night.id) is None
    assert VoteRepo.get_one_or_none(vote.id) is None


def test_game_nights_api_delete_as_anon(
    clean_db_context: Context, client_as_anon: TestClient
) -> None:
    game_night = DataService.create_game_night()

    response = client_as_anon.delete(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTP_401_UNAUTHORIZED

    assert GameNightRepo.get(game_night.id) is not None


def test_game_nights_api_post_recalculate_sums_as_admin(
    clean_db_context: Context, client_as_admin: TestClient
) -> None:
    game_night = DataService.create_game_night(sum_=None)
    DataService.create_vote(game_night=game_night, appetizer=1, main_course=1, dessert=1, game=1)

    response = client_as_admin.post("/api/gamenights/actions/recalculate-sum/")
    assert response.status_code == HTTP_200_OK

    assert GameNightRepo.get(game_night.id).sum == 1


def test_game_nights_api_post_recalculate_sums_as_anon(
    clean_db_context: Context, client_as_anon: TestClient
) -> None:
    response = client_as_anon.post("/api/gamenights/actions/recalculate-sum/")
    assert response.status_code == HTTP_401_UNAUTHORIZED


def test_game_nights_api_get_many(clean_db_context: Context, client_as_anon: TestClient) -> None:
    # Setup
    gn1 = DataService.create_game_night()
    DataService.create_vote(game_night=gn1)

    gn2 = DataService.create_game_night()
    DataService.create_vote(game_night=gn2)
    DataService.create_vote(game_night=gn2)

    # Test
    response = client_as_anon.get("/api/gamenights/")
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert len(data) == 2
    assert len(data[0]["votes"]) == 1
    assert len(data[1]["votes"]) == 2


def test_game_nights_api_get_one(clean_db_context: Context, client_as_anon: TestClient) -> None:
    game_night = DataService.create_game_night()

    response = client_as_anon.get(f"/api/gamenights/{game_night.id}/")
    assert response.status_code == HTTP_200_OK
    assert response.json()["id"] == game_night.id
