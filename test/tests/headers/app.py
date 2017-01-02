import falcon
import falconraml


class Dummy(object):
    def on_get(self, request, response):
        pass


api = falcon.API(middleware=[
    falconraml.ParameterChecker('test/tests/headers/spec.raml'),
])


api.add_route('/required/string', Dummy())
api.add_route('/required/number', Dummy())
api.add_route('/required/integer', Dummy())
api.add_route('/required/boolean', Dummy())
api.add_route('/nonrequired/mixed', Dummy())
