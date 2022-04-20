from securionpay.resource import Resource


class Credits(Resource):
    def create(self, params):
        return self._post("/credits", params)

    def get(self, credit_id):
        return self._get("/credits/%s" % credit_id)

    def update(self, credit_id, params):
        return self._post("/credits/%s" % credit_id, params)

    def list(self, params=None):
        return self._get("/credits", params)
