import falcon
import falconraml


class Dummy(object):
    def on_get(self, request, response, some_id):
        pass


api = falcon.API(middleware=[
    falconraml.ParameterChecker('test/tests/templatedpath/spec.raml'),
])


api.add_route('/templated/{some_id}', Dummy())
