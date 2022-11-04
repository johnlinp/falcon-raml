import falcon
import falconraml


class Dummy(object):
    def on_post(self, request, response):
        pass


api = falcon.API(middleware=[
    falconraml.ParameterChecker('test/tests/nojsontranslator/spec.raml'),
])


api.add_route('/basic/string', Dummy())
