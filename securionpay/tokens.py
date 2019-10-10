from securionpay.resource import Resource


class Tokens(Resource):
    def create(self, params):
        return self._post("/tokens", params)

    def get(self, token_id):
        return self._get("/tokens/%s" % token_id)
