from flask import g, jsonify
from test.testdata import TEST_DATA_PARSED_XML, TEST_DATA_OVERVIEW


def _get_client():
    if not hasattr(g, 'client'):
        # TODO: init client mysql, mongodb, ...
        client = "TODO"
        g.client = client

    return client


def update(user, data):
    client = _get_client()
    pass


def upload(user, data):
    client = _get_client()


def test_data_uploaded_data():
    # return test data
    TEST_DATA_PARSED_XML.tracking_data().id = 1
    return TEST_DATA_PARSED_XML


def test_data_uploaded_data_overview():
    # return test data
    return TEST_DATA_OVERVIEW
