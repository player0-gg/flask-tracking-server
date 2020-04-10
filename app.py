from flask import Flask, request, abort, jsonify


app = Flask(__name__)


@app.route('/api/uploaded_data', methods=['GET'])
def uploaded_data():
    # if not request.json:
    #     abort(400)

    return jsonify(text='success')


@app.route('/api/uploaded_data/<data_id>', methods=['GET'])
def uploaded_data_by_id(data_id):
    print('id {}'.format(data_id))
    # load test data
    return jsonify(text='success', data='')


@app.route('/api/upload', methods=['POST'])
def upload():
    # if not request.json:
    #     abort(400)

    return jsonify(text='success')


@app.route('/api/remove', methods=['POST'])
def remove():
    # if not request.json:
    #     abort(400)

    return jsonify(text='success')


if __name__ == '__main__':
    app.run(debug=True)

