import falcon
import falcon.testing
from tests.templatedpath import app


class TestTemplatedPath(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/templated/9527'
        self.query_param_name = 'required_string'
        self.query_param_value = 'hello'

    def test_success(self):
        response = self.simulate_get(self.path, params={
            self.query_param_name: self.query_param_value,
        })
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_query_params(self):
        response = self.simulate_get(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.query_param_name)
        )
