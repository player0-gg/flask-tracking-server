from flask import request, abort
from functools import wraps
from lib import Errors


def preprocess_request(arg_type='json', required_args=[], preprocessors=[]):

    def from_json():
        return request.get_json()

    def from_args():
        return request.args

    def from_values():
        return request.values

    # set get_data method depends on the arguments type in the request
    if arg_type == 'json':
        # we want to use json
        get_data = from_json
    elif arg_type == 'values':
        # the request from angular web app contains the arguments in values?
        get_data = from_values
    else:
        get_data = from_args

    def decorator_validate_and_process_data(func):
        @wraps(func)
        def wrapper_extract_and_process_data(**kwargs):
            data = get_data().copy()
            # validate request data
            missing_keys = []
            for key in required_args:
                if key not in data:
                    missing_keys.append(key)
            if len(missing_keys) > 0:
                abort(400, 'Missing key: {}'.format(missing_keys[0]))
                # abort(400, 'Missing keys: {}'.format(missing_keys))

            # update data using preprocessors
            for preprocessor in preprocessors:
                preprocessor(data)
            # we put the data as the first argument to the function, which uses this decorator
            return func(data, **kwargs)

        return wrapper_extract_and_process_data

    return decorator_validate_and_process_data


def login_required(func):
    @wraps(func)
    def wrapper_login_required(*args, **kwargs):
        # TODO: find the user in db and set to g.user
        if g.user is None:
            raise Errors.LOGIN_REQUIRED
        return func(*args, **kwargs)

    return wrapper_login_required
