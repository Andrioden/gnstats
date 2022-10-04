import pytest
from google.cloud.ndb import Client

from tests.helpers import clean_db


@pytest.fixture(scope="function")
def clean_db_context() -> None:
    with Client().context() as c:
        clean_db()
        yield c
        clean_db()
