import json
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from lib import Errors
from test.testdata import TEST_DATA_PARSED_XML
from lib import Database
from auth import auth


app = Flask(__name__)
app.register_blueprint(auth)
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
    return _data_as_response(Database.test_data_uploaded_data(data_id))


def _data_as_response(data):
    # return jsonify(json=json.dumps(data.to_dict()))
    return json.dumps(data.to_dict())


@app.route('/api/update', methods=['POST'])
def update():
    if request.json:
        data = request.get_json()
    else:
        # because of formData in angular?
        data = request.values
    user = {'id': 1}
    Database.update(user, data)
    return jsonify(text='success')


@app.route('/api/upload', methods=['POST'])
def upload():
    # parser data to sql
    user, data = _parse_data_from_upload_request()
    # return Database.upload(user, data)
    return _data_as_response(Database.test_data_uploaded_data(1))


def _parse_data_from_upload_request():
    # TODO: use wrapper instead
    # if not request.json:
    #     abort(400)
    user = {'id': 1}
    data = TEST_DATA_PARSED_XML

    return user, data


@app.route('/api/remove/<data_id>', methods=['POST'])
def remove(data_id):
    # if not request.json:
    #     abort(400)

    # user, data
    Database.remove_data(int(float(data_id)))
    return jsonify(text='success')


if __name__ == '__main__':
    app.run(debug=True)

