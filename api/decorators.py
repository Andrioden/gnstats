from functools import wraps
from .utils import *
import logging

DECORATOR_NO_REQUEST_ATTRIBUTE_HELP_TEXT = "You have used the decorator on something that does not have a request attribute. Have you used it on the class instead of the class get/post function?"


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