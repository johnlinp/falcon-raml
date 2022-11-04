import falcon
import falcon.testing
from tests.headers import app


class TestHeadersRequiredString(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/string'
        self.header_name = 'X-Required-String'
        self.header_values = [
            'hello',
            r'!@#$%^&*(){}',
        ]

    def test_success(self):
        for value in self.header_values:
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_header(self):
        response = self.simulate_get(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing header value')
        self.assertEqual(
            response.json['description'],
            'The {} header is required.'.format(self.header_name)
        )

    def test_wrong_header(self):
        response = self.simulate_get(self.path, headers={
            'X-Wrong-Header': self.header_values[0],
        })
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing header value')
        self.assertEqual(
            response.json['description'],
            'The {} header is required.'.format(self.header_name)
        )

    def test_with_empty_string(self):
        response = self.simulate_get(self.path, headers={
            self.header_name: '',
        })
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_with_number(self):
        response = self.simulate_get(self.path, headers={
            self.header_name: '42',
        })
        # number strings are strings too
        self.assertEqual(response.status, falcon.HTTP_200)


class TestHeadersRequiredNumber(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/number'
        self.header_name = 'X-Required-Number'
        self.header_values = [
            '55.66',
            '42',
            '0',
            '-55.66',
        ]

    def test_success(self):
        for value in self.header_values:
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_header(self):
        response = self.simulate_get(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing header value')
        self.assertEqual(
            response.json['description'],
            'The {} header is required.'.format(self.header_name)
        )

    def test_not_numbers(self):
        wrong_values = [
            'hello',
            'a123',
            '123a',
        ]

        for value in wrong_values:
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid header value')
            self.assertEqual(
                response.json['description'],
                'The value provided for the {} header is invalid. '
                'Should be a number.'.format(self.header_name)
            )


class TestHeadersRequiredInteger(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/integer'
        self.header_name = 'X-Required-Integer'
        self.header_values = [
            '42',
            '0',
            '-42',
        ]

    def test_success(self):
        for value in self.header_values:
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_header(self):
        response = self.simulate_get(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing header value')
        self.assertEqual(
            response.json['description'],
            'The {} header is required.'.format(self.header_name)
        )

    def test_not_integers(self):
        wrong_values = [
            'hello',
            '55.66',
        ]

        for value in wrong_values:
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid header value')
            self.assertEqual(
                response.json['description'],
                'The value provided for the {} header is invalid. '
                'Should be an integer.'.format(self.header_name)
            )


class TestHeadersRequiredBoolean(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/required/boolean'
        self.header_name = 'X-Required-Boolean'
        self.header_values = [
            'true',
            'false',
        ]

    def test_success(self):
        for value in self.header_values:
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_200)

    def test_missing_header(self):
        response = self.simulate_get(self.path)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Missing header value')
        self.assertEqual(
            response.json['description'],
            'The {} header is required.'.format(self.header_name)
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
            response = self.simulate_get(self.path, headers={
                self.header_name: value,
            })
            self.assertEqual(response.status, falcon.HTTP_400)
            self.assertEqual(response.json['title'], 'Invalid header value')
            self.assertEqual(
                response.json['description'],
                'The value provided for the {} header is invalid. '
                'Should be "true" or "false".'.format(self.header_name)
            )


class TestHeadersNonRequiredMixed(falcon.testing.TestCase):
    def setUp(self):
        self.app = app.api
        self.path = '/nonrequired/mixed'
        self.string_header_name = 'X-Non-Required-String'
        self.number_header_name = 'X-Non-Required-Number'
        self.integer_header_name = 'X-Non-Required-Integer'
        self.boolean_header_name = 'X-Non-Required-Boolean'
        self.string_header_value = 'hello'
        self.number_header_value = '55.66'
        self.integer_header_value = '42'
        self.boolean_header_value = 'true'

    def test_no_headers(self):
        response = self.simulate_get(self.path, headers={})
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_all_headers(self):
        response = self.simulate_get(self.path, headers={
            self.string_header_name: self.string_header_value,
            self.number_header_name: self.number_header_value,
            self.integer_header_name: self.integer_header_value,
            self.boolean_header_name: self.boolean_header_value,
        })
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_only_string(self):
        response = self.simulate_get(self.path, headers={
            self.string_header_name: self.string_header_value,
        })
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_wrong_number(self):
        response = self.simulate_get(self.path, headers={
            self.string_header_name: self.string_header_value,
            self.number_header_name: 'hey',
            self.integer_header_name: self.integer_header_value,
            self.boolean_header_name: self.boolean_header_value,
        })
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json['title'], 'Invalid header value')
        self.assertEqual(
            response.json['description'],
            'The value provided for the {} header is invalid. '
            'Should be a number.'.format(self.number_header_name)
        )
