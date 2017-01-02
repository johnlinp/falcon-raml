import falcon
import falconraml


class Dummy(object):
    def on_post(self, request, response):
        pass


api = falcon.API(middleware=[
    falconraml.JsonTranslator(),
    falconraml.ParameterChecker('test/tests/jsonbody/spec.raml'),
])


api.add_route('/simple/string', Dummy())
api.add_route('/malformed/schema', Dummy())
