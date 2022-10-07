from functools import wraps
from typing import Any, Callable

from google.cloud.ndb import Client, get_context


def ensure_db_context(func: Callable) -> Callable:
    @wraps(func)
    def wrapper_do_twice(*args: Any, **kwargs: Any) -> Callable:
        if get_context(False):
            return func(*args, **kwargs)
        else:
            with Client().context():
                return func(*args, **kwargs)

    return wrapper_do_twice
