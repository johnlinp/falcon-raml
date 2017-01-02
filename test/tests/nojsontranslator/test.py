import falcon
import falcon.testing
import json
from tests.nojsontranslator import app


class TestNoJsonTranslator(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/basic/string'
        self.field_name = 'some_string'
        self.field_value = 'hello'

    def test_error(self):
        response = self.simulate_post(self.path, headers={
            'Content-Type': 'application/json',
        }, body=json.dumps({
            self.field_name: self.field_value,
        }))
        self.assertEqual(response.status, falcon.HTTP_500)
        self.assertEqual(response.json['title'], 'Internal server error')
        self.assertEqual(
            response.json['description'],
            'Please use falconraml.JsonTranslator to parse json body.'
        )
