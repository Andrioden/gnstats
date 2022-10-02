from functools import wraps

from google.cloud import ndb
from google.cloud.ndb import get_context

from .utils import *
import logging

DECORATOR_NO_REQUEST_ATTRIBUTE_HELP_TEXT = "You have used the decorator on something that does not have a request attribute. Have you used it on the class instead of the class get/post function?"


def ensure_db_context(func):
    @wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        if get_context(False):
            return func(*args, **kwargs)
        else:
            with ndb.Client().context():
                return func(*args, **kwargs)
    return wrapper_do_twice


def require_verified(func):
    @wraps(func)
    def wrapper(request_handler, *args):
        if not hasattr(request_handler, 'request'):
            raise Exception(DECORATOR_NO_REQUEST_ATTRIBUTE_HELP_TEXT)

        if not validate_verified(request_handler.response):
            return None
        else:
            return func(request_handler, *args)
    return wrapper


def require_admin(func):
    @wraps(func)
    def wrapper(request_handler, *args):
        if not hasattr(request_handler, 'request'):
            raise Exception(DECORATOR_NO_REQUEST_ATTRIBUTE_HELP_TEXT)

        if not validate_admin(request_handler.response):
            return None
        else:
            return func(request_handler, *args)
    return wrapper


def require_request_data(required_data):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(request_handler, *args):
            if not hasattr(request_handler, 'request'):
                raise Exception(DECORATOR_NO_REQUEST_ATTRIBUTE_HELP_TEXT)

            if not validate_request_data(request_handler, required_data):
                return None
            else:
                return func(request_handler, *args)
        return wrapper
    return actual_decorator