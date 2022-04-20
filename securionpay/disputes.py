from securionpay.resource import Resource


class Disputes(Resource):
    def get(self, dispute_id):
        return self._get("/disputes/%s" % dispute_id)

    def update(self, dispute_id, params):
        return self._post("/disputes/%s" % dispute_id, params)

    def close(self, dispute_id):
        return self._post("/disputes/%s/close" % dispute_id)

    def list(self, params=None):
        return self._get("/disputes", params)
