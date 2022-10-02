from fastapi.testclient import TestClient

from api.app import app
from api.decorators import ensure_db_context
from models import GameNight
from tests.data_service import DataService

client = TestClient(app)


@ensure_db_context
def test_read_main():
    DataService.create_game_night()

    response = client.get("/gamenights")
    assert response.status_code == 200
    assert len(response.json()) > 0
