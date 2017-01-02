import falcon
import falcon.testing
import urllib.parse
from tests.formbody import app


class TestFormBodyRequiredString(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/string'
        self.form_param_name = 'required_string'
        self.form_param_values = [
            'hello',
            r'!@#$%^&*(){}',
        ]
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def test_success(self):
        for value in self.form_param_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_content_type(self):
        response = self.simulate_post(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Bad request')
        self.assertEqual(response.json['description'], 'No content type')

    def test_missing_form_body(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.form_param_name)
        )

    def test_wrong_param(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=urllib.parse.urlencode({
                'wrong_param': self.form_param_values[0],
            })
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.form_param_name)
        )

    def test_with_empty_string(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=urllib.parse.urlencode({
                self.form_param_name: '',
            })
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.form_param_name)
        )

    def test_with_number(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=urllib.parse.urlencode({
                self.form_param_name: '42',
            })
        )
        # number strings are strings too
        self.assertEqual(response.status, falcon.HTTP_200)


class TestFormBodyRequiredNumber(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/number'
        self.form_param_name = 'required_number'
        self.form_param_values = [
            '55.66',
            '42',
            '0',
            '-55.66',
        ]
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def test_success(self):
        for value in self.form_param_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_form_body(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.form_param_name)
        )

    def test_not_numbers(self):
        wrong_values = [
            'hello',
            'a123',
            '123a',
        ]

        for value in wrong_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid parameter')
            self.assertEqual(
                response.json['description'],
                'The "{}" parameter is invalid. '
                'Should be a number.'.format(self.form_param_name)
            )


class TestFormBodyRequiredInteger(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/integer'
        self.form_param_name = 'required_integer'
        self.form_param_values = [
            '42',
            '0',
            '-42',
        ]
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def test_success(self):
        for value in self.form_param_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_form_body(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.form_param_name)
        )

    def test_not_integers(self):
        wrong_values = [
            'hello',
            '55.66',
        ]

        for value in wrong_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid parameter')
            self.assertEqual(
                response.json['description'],
                'The "{}" parameter is invalid. '
                'Should be an integer.'.format(self.form_param_name)
            )


class TestFormBodyRequiredBoolean(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/boolean'
        self.form_param_name = 'required_boolean'
        self.form_param_values = [
            'true',
            'false',
        ]
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def test_success(self):
        for value in self.form_param_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_form_body(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.form_param_name)
        )

    def test_not_booleans(self):
        wrong_values = [
            'hello',
            'TRUE',
            'FALSE',
            'yes',
            'no',
        ]

        for value in wrong_values:
            response = self.simulate_post(
                self.path,
                headers=self.headers,
                body=urllib.parse.urlencode({
                    self.form_param_name: value,
                })
            )
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid parameter')
            self.assertEqual(
                response.json['description'],
                'The "{}" parameter is invalid. '
                'Should be "true" or "false".'.format(self.form_param_name)
            )


class TestFormBodyNonRequiredMixed(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/nonrequired/mixed'
        self.string_query_param_name = 'non_required_string'
        self.number_query_param_name = 'non_required_number'
        self.integer_query_param_name = 'non_required_integer'
        self.boolean_query_param_name = 'non_required_boolean'
        self.string_query_param_value = 'hello'
        self.number_query_param_value = '55.66'
        self.integer_query_param_value = '42'
        self.boolean_query_param_value = 'true'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def test_no_form_body(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
        )
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_all_params(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=urllib.parse.urlencode({
                self.string_query_param_name: self.string_query_param_value,
                self.number_query_param_name: self.number_query_param_value,
                self.integer_query_param_name: self.integer_query_param_value,
                self.boolean_query_param_name: self.boolean_query_param_value,
            })
        )
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_only_string(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=urllib.parse.urlencode({
                self.string_query_param_name: self.string_query_param_value,
            })
        )
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_wrong_number(self):
        response = self.simulate_post(
            self.path,
            headers=self.headers,
            body=urllib.parse.urlencode({
                self.string_query_param_name: self.string_query_param_value,
                self.number_query_param_name: 'hey',
                self.integer_query_param_name: self.integer_query_param_value,
                self.boolean_query_param_name: self.boolean_query_param_value,
            })
        )
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Invalid parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is invalid. '
            'Should be a number.'.format(self.number_query_param_name)
        )
