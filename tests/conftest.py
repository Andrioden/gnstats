from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from google.cloud.ndb import Client, Context

from api.app import app
from api.session import me_or_401
from tests.data_service import DataService
from tests.helpers import clean_db


@pytest.fixture(scope="session")
def db_context() -> Iterator[Context]:
    with Client().context() as context:
        yield context


@pytest.fixture(scope="function")
def clean_db_context(db_context: Context) -> Iterator[Context]:
    clean_db()
    yield db_context
    clean_db()


@pytest.fixture(scope="function")
def client_as_anon() -> Iterator[TestClient]:
    yield TestClient(app)


@pytest.fixture(scope="function")
def client_as_deactivated() -> Iterator[TestClient]:
    app.dependency_overrides[me_or_401] = DataService.build_deactivated_person
    yield TestClient(app)
    app.dependency_overrides = {}


@pytest.fixture(scope="function")
def client_as_activated() -> Iterator[TestClient]:
    app.dependency_overrides[me_or_401] = DataService.build_activated_person
    yield TestClient(app)
    app.dependency_overrides = {}


@pytest.fixture(scope="function")
def client_as_admin() -> Iterator[TestClient]:
    app.dependency_overrides[me_or_401] = DataService.build_admin_person
    yield TestClient(app)
    app.dependency_overrides = {}
