from flask import Blueprint, jsonify, abort, request
import lib.wrapper as wrapper
from lib import Database


auth = Blueprint('auth', __name__)

REQUIRED_LOGIN = ['email', 'password']
REQUIRED_REGISTRATION = ['email', 'password', 'name']
REQUIRED_LOGGED_IN = ['user_id', 'login_token']


@auth.route('/login', methods=['POST'])
@wrapper.preprocess_request(required_args=REQUIRED_LOGIN)
def login(preprocessed_data):
    print('email: {}'.format(preprocessed_data['email']))
    user_entry = Database.find_user({'email': 'test@test.test'})
    if user_entry is None:
        abort(400, 'User not found')
    login_token = user_entry['login_token']
    return jsonify(login_token=login_token)


@auth.route('/register', methods=['POST'])
@wrapper.preprocess_request(required_args=REQUIRED_LOGIN)
def register(preprocessed_data):
    login_token = 'asd'
    return jsonify(login_token=login_token)


