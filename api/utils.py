import json
import logging
from datetime import date, datetime
from typing import Optional

from google.appengine.api import users

from models.db.person import Person


def ok_200(response, data):
    response.headers["Content-Type"] = "application/json"
    response.out.write(json.dumps(data))


def ok_204(response):
    response.set_status(204)


def error(status, response, code, message):
    response.headers["Content-Type"] = "application/json"
    response.set_status(status)
    response.out.write(json.dumps({"error_code": code, "error_message": message}))


def unauthorized_401(response, code, message):
    error(401, response, code, message)


def forbidden_403(response, code, message):
    error(403, response, code, message)


# def validate_verified(response):
#     user = users.get_current_user()
#     if not user:
#         unauthorized_401(response, "VALIDATION_ERROR_NOT_LOGGED_INN", "The browsing user is not logged in.")
#         return False
#
#     person = Person.query(Person.userid == user.user_id()).get()
#     if not person:
#         unauthorized_401(response, "VALIDATION_ERROR_NOT_VERIFIED", "The browsing user is logged in with a google account, but has not verified it.")
#         return False
#     return True


def validate_admin(response):
    if not users.is_current_user_admin():
        forbidden_403(
            response,
            "VALIDATION_ERROR_NOT_ADMIN",
            "The browsing user is logged in and authenticated, but does not have admin permissions.",
        )
        return False
    else:
        return True


def validate_request_data(request_handler, required_data):
    try:
        request_data = json.loads(request_handler.request.body)
    except ValueError:
        error(
            400,
            request_handler.response,
            "VALIDATION_ERROR_MISSING_DATA",
            "The request has no request body when required data is: " + ", ".join(required_data),
        )
        return False

    for key in required_data:
        if request_data.get(key, None) in [None, ""]:
            error(
                400,
                request_handler.response,
                "VALIDATION_ERROR_MISSING_DATA",
                "The request body is missing the data value '%s'" % key,
            )
            return False
    return True


def date_to_epoch(date_value):
    if type(date_value) is date:
        return int((date_value - date(1970, 1, 1)).total_seconds())
    elif type(date_value) is datetime:
        return int((date_value - datetime(1970, 1, 1)).total_seconds())
    else:
        raise Exception("Type not handled: " + type(date_value).__name__)


def current_user_person():
    # users.
    user = users.get_current_user()
    return Person.query(Person.userid == user.user_id()).get()


def current_user_person_name():
    return "André"
    # user = users.get_current_user()
    # if not user:
    #     return None
    # else:
    #     person = Person.query(Person.userid == user.user_id()).get()
    #     if person:
    #         return person.name
    #     else:
    #         return None


def me_person() -> Optional[Person]:
    # Hardcode, remove!!!
    return Person.query(Person.name == "André").get()
    # Keep
    # if user := users.get_current_user():
    #     return Person.query(Person.userid == user.user_id()).get()
    # else:
    #     return None
