#!/usr/bin/env python

import logging
import api.constants as constants
from flask import Flask, jsonify, g
from flask_cors import CORS
from pymongo import MongoClient
from mongoframes import Frame
from api.routes.pdv import pdv

client = MongoClient(
    host=constants.MONGO_HOST,
    port=constants.MONGO_PORT,
    username=constants.MONGO_USER,
    password=constants.MONGO_PASSWORD
)

db = client[constants.MONGO_DB]

app = Flask(__name__)

CORS(app)


def setup_db():
    g.db = db
    g.mongo_client = client
    Frame._client = client


app.before_request(setup_db)
app.register_blueprint(pdv)


@app.route("/", methods=['GET'])
def route_index():
    return jsonify({
        'apiVersion': 1.0
    })


@app.errorhandler(KeyError)
def handle_key_error(error):
    error = {'message': 'Missing required parameter: {}'.format(error.message)}
    return jsonify({'error': error}), 500


@app.errorhandler(Exception)
def handle_exception(error):
    logging.warning('Error happened in request: {}'.format(str(error)))
    import traceback
    traceback.print_exc()
    error = {'message': str(error), 'type': str(type(error).__name__)}
    return jsonify({'error': error}), 500


@app.before_first_request
def setup_logging():
    if not app.debug:
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)
