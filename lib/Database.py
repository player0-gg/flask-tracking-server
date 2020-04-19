from flask import g, jsonify
from lib import Errors
from test.testdata import TEST_DATA_PARSED_XML, TEST_DATA_OVERVIEW
from os import environ
from pymongo import MongoClient


def _get_client():
    if not hasattr(g, 'mongodb_client'):
        # TODO: init environment (dev, testing, prod)
        client = MongoClient(environ.get('MONGODB_CLIENT_CONFIG'))
        g.mongodb_client = client

    return g.mongodb_client


def _get_db():
    client = _get_client()
    if not hasattr(g, 'db_test'):
        g.db_test = client.test
    return g.db_test


def find_user(user):
    mongodb_test = _get_db()
    return mongodb_test.users.find_one({'email': user['email']})


# TODO: add test mode environment

def update(user, data):
    client = _get_client()
    _update_test_data(user, data)


def upload(user, data):
    client = _get_client()


def remove_data(data_id):
    _remove_test_data(int(float(data_id)))


# TODO: add test mode environment
def _update_test_data(user, data):
    data_id = data.get('tracking_id')
    if data_id is None:
        raise Errors.UPDATE_TRACK_DATA_INVALID

    tracking_data, position = _find_data_in_test_db(data_id)
    if tracking_data is None:
        raise Errors.DATA_NOT_FOUND

    comment = data.get('comment')
    if comment:
        tracking_data['comment'] = comment

    title = data.get('title')
    if title:
        tracking_data['title'] = title


def test_data_uploaded_data(data_id):
    tracking_data, position = _find_data_in_test_db(data_id)
    # return test data
    TEST_DATA_PARSED_XML.id = data_id
    TEST_DATA_PARSED_XML.title = tracking_data['title']
    TEST_DATA_PARSED_XML.comment = tracking_data['comment']
    return TEST_DATA_PARSED_XML


def test_data_uploaded_data_overview():
    mongodb_test = _get_db()
    user_entry = mongodb_test.users.find_one({'name': 'tester1'})
    print('user_entry = {}'.format(user_entry))

    # return test data
    return TEST_DATA_OVERVIEW


def _remove_test_data(data_id):
    tracking_data, position = _find_data_in_test_db(data_id)
    if tracking_data:
        del TEST_DATA_OVERVIEW[position]


def _find_data_in_test_db(data_id):
    track = None
    position = 0
    for x in TEST_DATA_OVERVIEW:
        if x['id'] == int(data_id):
            track = x
            break
        position += 1
    return track, position
