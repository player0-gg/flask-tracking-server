from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from lib import Errors
from test.testdata import TEST_DATA_PARSED_XML
from lib import Database
import json


app = Flask(__name__)
CORS(app)


@app.errorhandler(Errors.Error)
def handle_app_errors(err):
    return err.http_error()


@app.route('/api/uploaded_data', methods=['GET'])
def uploaded_data():
    # if not request.json:
    #     abort(400)

    # return jsonify(json=json.dumps(Database.test_data_uploaded_data_overview()))
    return json.dumps(Database.test_data_uploaded_data_overview())


@app.route('/api/uploaded_data/<data_id>', methods=['GET'])
def uploaded_data_by_id(data_id):
    print('id {}'.format(data_id))
    # load test data
    return _data_as_response(Database.test_data_uploaded_data())


def _data_as_response(data):
    # return jsonify(json=json.dumps(data.to_dict()))
    return json.dumps(data.to_dict())


@app.route('/api/update', methods=['POST'])
def update():
    # if not request.json:
    #     abort(400)

    # return jsonify(json=json.dumps(Database.test_data_uploaded_data_overview()))
    return json.dumps(Database.test_data_uploaded_data_overview())


@app.route('/api/upload', methods=['POST'])
def upload():
    # parser data to sql
    user, data = _parse_data_from_upload_request()
    # return Database.upload(user, data)
    return _data_as_response(Database.test_data_uploaded_data())


def _parse_data_from_upload_request():
    # if not request.json:
    #     abort(400)
    user = {'id': 1}
    data = TEST_DATA_PARSED_XML

    return user, data


@app.route('/api/remove', methods=['POST'])
def remove():
    # if not request.json:
    #     abort(400)

    return jsonify(text='success')


if __name__ == '__main__':
    app.run(debug=True)

