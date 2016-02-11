import json
from google.appengine.api import users
from datetime import datetime
from models import Person


def error_400(response, code, message):
    response.headers['Content-Type'] = 'application/json'
    response.set_status(400)
    response.out.write(json.dumps({'error_code': code, 'error_message': message}))


def unauthorized_401(response, code, message):
    response.headers['Content-Type'] = 'application/json'
    response.set_status(401)
    response.out.write(json.dumps({'error_code': code, 'error_message': message}))


def forbidden_403(response, code, message):
    response.headers['Content-Type'] = 'application/json'
    response.set_status(403)
    response.out.write(json.dumps({'error_code': code, 'error_message': message}))


def validate_authenticated(response):
    user = users.get_current_user()
    if users.is_current_user_admin():
        return True
    elif not user:
        unauthorized_401(response, "VALIDATION_ERROR_NOT_LOGGED_INN", "The browsing user is not logged in.")
        return False

    person = Person.query(Person.userid == user.user_id()).get()
    if not person:
        unauthorized_401(response, "VALIDATION_ERROR_NOT_CLAIMED", "The browsing user is logged in with a google account, but has not verified it.")
        return False
    return True


# def validate_logged_in_admin(response):
#     if not users.is_current_user_admin():
#         forbidden_403(response, "VALIDATION_ERROR_MISSING_ADMIN_PERMISSION", "The browsing user is logged in and authenticated, but does not have admin permissions.")
#         return False
#     else:
#         return True


def validate_request_data(response, data_dict, list_of_dict_keys):
    for key in list_of_dict_keys:
        if data_dict.get(key, None) in [None, '']:
            error_400(response, "VALIDATION_ERROR_MISSING_DATA", "The request data is missing the input value '%s'" % key)
            return False
    return True


def date_to_epoch(date_value):
    return int((date_value - datetime(1970,1,1)).total_seconds())


def set_json_response(response, data):
    response.headers['Content-Type'] = 'application/json'
    response.out.write(json.dumps(data))