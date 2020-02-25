import os
import sys
import json
from mongoframes import Frame
from urllib.parse import urlencode
from flask import Flask, g, jsonify
from pymongo import MongoClient
from mongomock import MongoClient as MongoClientMock

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
import api.constants as constants


def setup_db():
    client = MongoClient(
        host=constants.MONGO_HOST,
        port=constants.MONGO_PORT,
        username=constants.MONGO_USER,
        password=constants.MONGO_PASSWORD
    )
    db = client[constants.MONGO_DB]
    Frame._client = client
    return db


def setup_mock_db():
    client = MongoClientMock(
        host=constants.MONGO_HOST,
        port=constants.MONGO_PORT,
        username=constants.MONGO_USER,
        password=constants.MONGO_PASSWORD
    )
    db = client[constants.MONGO_DB]
    Frame._client = client
    return db


def create_flask_app(mock=False, db=None):
    if db is None:
        if mock:
            db = setup_mock_db()
        else:
            db = setup_db()

    def before_setup_db():
        g.db = db
    app = Flask(__name__)
    app.before_request(before_setup_db)

    @app.errorhandler(KeyError)
    def handle_key_error(error):
        error = {'message': 'Missing required parameter: {}'.format(error.message)}
        return jsonify({'error': error})

    @app.errorhandler(Exception)
    def handle_exception(error):
        error = {'message': str(error), 'type': str(type(error).__name__)}
        return jsonify({'error': error})

    return app


def api_request(app, endpoint, method, params=None):
    if params and method == 'get':
        endpoint += '?{}'.format(urlencode(params))
    if params is None and method != 'get':
        params = {}
    method = getattr(app, method)
    res = method(endpoint, data=json.dumps(params), content_type='application/json')
    data = res.data.decode("utf-8")
    if data[0] != '{':
        raise Exception('Invalid Response from API: {}'.format(data))
    return json.loads(data)
