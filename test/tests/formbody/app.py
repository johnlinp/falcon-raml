import falcon
import falconraml


class Dummy(object):
    def on_post(self, request, response):
        pass


api = falcon.API(middleware=[
    falconraml.JsonTranslator(),
    falconraml.ParameterChecker('test/tests/formbody/spec.raml'),
])


api.req_options.auto_parse_form_urlencoded = True


api.add_route('/required/string', Dummy())
api.add_route('/required/number', Dummy())
api.add_route('/required/integer', Dummy())
api.add_route('/required/boolean', Dummy())
api.add_route('/nonrequired/mixed', Dummy())
