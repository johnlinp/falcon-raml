import falcon
import falcon.testing
import json
from tests.jsonbody import app


class TestJsonBodySimpleString(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/simple/string'
        self.field_name = 'some_string'
        self.field_values = [
            'hello',
            r'!@#$%^&*(){}',
        ]
        self.headers = {
            'Content-Type': 'application/json',
        }

    def test_success(self):
        for value in self.field_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=json.dumps({
                    self.field_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_not_a_string(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=json.dumps({
                self.field_name: 42,
            })
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Bad request body')
        self.assertEqual(
            response.json['description'],
            "42 is not of type 'string'"
        )

    def test_missing_content_type(self):
        response = self.simulate_post(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Bad request')
        self.assertEqual(response.json['description'], 'No content type')

    def test_missing_body(self):
        response = self.simulate_post(self.path, headers=self.headers)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Bad request body')
        self.assertEqual(
            response.json['description'],
            "None is not of type 'object'"
        )

    def test_empty_object(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body='{}'
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Bad request body')
        self.assertEqual(
            response.json['description'],
            "'some_string' is a required property".format(self.field_name)
        )


class TestJsonBodyMalformedSchema(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/malformed/schema'
        self.field_name = 'some_string'
        self.field_value = 'hello'
        self.headers = {
            'Content-Type': 'application/json',
        }

    def test_error(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=json.dumps({
                self.field_name: self.field_value,
            })
        )
        self.assertEqual(response.status, falcon.HTTP_500)
        self.assertEqual(response.json['title'], 'Internal server error')
        self.assertEqual(
            response.json['description'],
            'Failed to parse jsonschema.'
        )
