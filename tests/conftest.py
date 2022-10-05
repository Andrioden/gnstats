from typing import Iterator

import pytest
from google.cloud.ndb import Client, Context

from tests.helpers import clean_db


@pytest.fixture(scope="function")
def clean_db_context() -> Iterator[Context]:
    with Client().context() as c:
        clean_db()
        yield c
        clean_db()
