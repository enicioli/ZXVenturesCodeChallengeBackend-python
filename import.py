#!/usr/bin/env python

from pymongo import MongoClient
from mongoframes import Frame
import api.constants as constants
from api.models.pdv import PDVModel
from api.odm.pdv import PDVDocument
import json
import pymongo

client = MongoClient(
    host=constants.MONGO_HOST,
    port=constants.MONGO_PORT,
    username=constants.MONGO_USER,
    password=constants.MONGO_PASSWORD
)

db = client[constants.MONGO_DB]

Frame._client = client

json_file = open('./resources/pdv_collection.json')
data = json.load(json_file)
for pdv in data['pdvs']:
    PDVModel.create_pdv(pdv)

PDVDocument.get_collection().create_index([('id', pymongo.ASCENDING)], unique=True)
PDVDocument.get_collection().create_index([('document', pymongo.ASCENDING)], unique=True)
PDVDocument.get_collection().create_index([('coverageArea', pymongo.GEOSPHERE)])
