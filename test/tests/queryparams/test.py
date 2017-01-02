import falcon
import falcon.testing
from tests.queryparams import app


class TestQueryParamRequiredString(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/string'
        self.query_param_name = 'required_string'
        self.query_param_values = [
            'hello',
            r'!@#$%^&*(){}',
        ]

    def test_success(self):
        for value in self.query_param_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
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

    def test_wrong_param(self):
        response = self.simulate_get(self.path, params={
            'wrong_param': self.query_param_values[0],
        })
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.query_param_name)
        )

    def test_with_empty_string(self):
        response = self.simulate_get(self.path, params={
            self.query_param_name: '',
        })
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is required.'.format(self.query_param_name)
        )

    def test_with_number(self):
        response = self.simulate_get(self.path, params={
            self.query_param_name: '42',
        })
        # number strings are strings too
        self.assertEqual(response.status, falcon.HTTP_200)


class TestQueryParamsRequiredNumber(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/number'
        self.query_param_name = 'required_number'
        self.query_param_values = [
            '55.66',
            '42',
            '0',
            '-55.66',
        ]

    def test_success(self):
        for value in self.query_param_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
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

    def test_not_numbers(self):
        wrong_values = [
            'hello',
            'a123',
            '123a',
        ]

        for value in wrong_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid parameter')
            self.assertEqual(
                response.json['description'],
                'The "{}" parameter is invalid. '
                'Should be a number.'.format(self.query_param_name)
            )


class TestQueryParamsRequiredInteger(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/integer'
        self.query_param_name = 'required_integer'
        self.query_param_values = [
            '42',
            '0',
            '-42',
        ]

    def test_success(self):
        for value in self.query_param_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
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

    def test_not_integers(self):
        wrong_values = [
            'hello',
            '55.66',
        ]

        for value in wrong_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid parameter')
            self.assertEqual(
                response.json['description'],
                'The "{}" parameter is invalid. '
                'Should be an integer.'.format(self.query_param_name)
            )


class TestQueryParamsRequiredBoolean(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/boolean'
        self.query_param_name = 'required_boolean'
        self.query_param_values = [
            'true',
            'false',
        ]

    def test_success(self):
        for value in self.query_param_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
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

    def test_not_booleans(self):
        wrong_values = [
            'hello',
            'TRUE',
            'FALSE',
            'yes',
            'no',
        ]

        for value in wrong_values:
            response = self.simulate_get(self.path, params={
                self.query_param_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid parameter')
            self.assertEqual(
                response.json['description'],
                'The "{}" parameter is invalid. '
                'Should be "true" or "false".'.format(self.query_param_name)
            )


class TestQueryParamsNonRequiredMixed(falcon.testing.TestCase):
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

    def test_no_params(self):
        response = self.simulate_get(self.path, params={})
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_all_params(self):
        response = self.simulate_get(self.path, params={
            self.string_query_param_name: self.string_query_param_value,
            self.number_query_param_name: self.number_query_param_value,
            self.integer_query_param_name: self.integer_query_param_value,
            self.boolean_query_param_name: self.boolean_query_param_value,
        })
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_only_string(self):
        response = self.simulate_get(self.path, params={
            self.string_query_param_name: self.string_query_param_value,
        })
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_wrong_number(self):
        response = self.simulate_get(self.path, params={
            self.string_query_param_name: self.string_query_param_value,
            self.number_query_param_name: 'hey',
            self.integer_query_param_name: self.integer_query_param_value,
            self.boolean_query_param_name: self.boolean_query_param_value,
        })
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Invalid parameter')
        self.assertEqual(
            response.json['description'],
            'The "{}" parameter is invalid. '
            'Should be a number.'.format(self.number_query_param_name)
        )
