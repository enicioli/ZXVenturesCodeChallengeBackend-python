import os
import sys
import json
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from tests import setup
from api.odm.pdv import PDVDocument
from api.models.pdv import PDVModel

db = setup.setup_mock_db()
app = setup.create_flask_app(mock=True, db=db)


class PDVModelTest(unittest.TestCase):
    def test_1_create_pdv(self):
        data = json.loads('{"address":{"coordinates":[-43.297337,-23.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName","tradingName":"test tradingName"}')
        pdv_entity = PDVModel.create_pdv(data)

        self.assertIsInstance(pdv_entity, PDVDocument)
        self.assertEqual(pdv_entity.address, data['address'])
        self.assertEqual(pdv_entity.coverageArea, data['coverageArea'])
        self.assertEqual(pdv_entity.document, data['document'])
        self.assertEqual(pdv_entity.ownerName, data['ownerName'])
        self.assertEqual(pdv_entity.tradingName, data['tradingName'])

    def test_2_update_pdv(self):
        pdv_entity = PDVDocument(json.loads('{"_id":"abc","address":{"coordinates":[-43.297337,-23.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName","tradingName":"test tradingName"}'))
        data = json.loads('{"address":{"coordinates":[-44.297337,-24.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName updated","tradingName":"test tradingName updated"}')
        pdv_entity_updated = PDVModel.update_pdv(pdv_entity, data)

        self.assertIsInstance(pdv_entity_updated, PDVDocument)
        self.assertEqual(pdv_entity_updated.address, data['address'])
        self.assertEqual(pdv_entity_updated.coverageArea, data['coverageArea'])
        self.assertEqual(pdv_entity_updated.document, data['document'])
        self.assertEqual(pdv_entity_updated.ownerName, data['ownerName'])
        self.assertEqual(pdv_entity_updated.tradingName, data['tradingName'])

    def test_3_get_pdv(self):
        data = json.loads('{"address":{"coordinates":[-43.297337,-23.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName","tradingName":"test tradingName","id":10000}')
        pdv_entity = PDVModel.create_pdv(data)
        pdv_entity_clone = PDVModel.get_pdv_by_id(pdv_entity.id)
        pdv_entity_not_exists = PDVModel.get_pdv_by_id(0)

        self.assertEqual(pdv_entity, pdv_entity_clone)
        self.assertIsNone(pdv_entity_not_exists)

    def test_4_delete_pdv(self):
        pdv_entity = PDVDocument(json.loads('{"_id":" ObjectId()","id":10000,"address":{"coordinates":[-43.297337,-23.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName","tradingName":"test tradingName"}'))
        result = PDVModel.delete_pdv(pdv_entity)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
