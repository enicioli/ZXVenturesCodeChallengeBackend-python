import os
import sys
import unittest
import json
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')

from tests.setup import *
from api.routes.pdv import pdv as pdv_app

db = setup_mock_db()
app = create_flask_app(mock=True, db=db)
app.register_blueprint(pdv_app, url_prefix='/pdv')


class RoutesUsersTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_1_create_pdv(self):
        data = json.loads('{"address":{"coordinates":[-43.297337,-23.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName","tradingName":"test tradingName","id":10000}')
        result = api_request(self.app, '/pdv', 'post', data)
        self.assertEqual(result['id'], 10000)

    def test_2_update_pdv(self):
        data = json.loads('{"address":{"coordinates":[-44.297337,-24.013538],"type":"Point"},"coverageArea":{"coordinates":[[[[-43.36556,-22.99669],[-43.36539,-23.01928],[-43.26583,-23.01802],[-43.25724,-23.00649],[-43.23355,-23.00127],[-43.2381,-22.99716],[-43.23866,-22.99649],[-43.24063,-22.99756],[-43.24634,-22.99736],[-43.24677,-22.99606],[-43.24067,-22.99381],[-43.24886,-22.99121],[-43.25617,-22.99456],[-43.25625,-22.99203],[-43.25346,-22.99065],[-43.29599,-22.98283],[-43.3262,-22.96481],[-43.33427,-22.96402],[-43.33616,-22.96829],[-43.342,-22.98157],[-43.34817,-22.97967],[-43.35142,-22.98062],[-43.3573,-22.98084],[-43.36522,-22.98032],[-43.36696,-22.98422],[-43.36717,-22.98855],[-43.36636,-22.99351],[-43.36556,-22.99669]]]],"type":"MultiPolygon"},"document":"07.526.557\/0001-00","ownerName":"test ownerName  updated","tradingName":"test tradingName updated","id":10000}')
        result = api_request(self.app, '/pdv/10000', 'put', data)
        self.assertEqual(result['address'], data['address'])

    def test_3_get_pdv(self):
        result = api_request(self.app, '/pdv/10000', 'get')
        self.assertEqual(result['id'], 10000)

    def test_4_delete_pdv(self):
        result = api_request(self.app, '/pdv/10000', 'delete')
        self.assertEqual(result['message'], 'OK')


if __name__ == "__main__":
    unittest.main()
