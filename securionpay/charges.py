from securionpay.resource import Resource


class Charges(Resource):
    def create(self, params):
        return self._post("/charges", params)

    def get(self, charge_id):
        return self._get("/charges/%s" % charge_id)

    def update(self, charge_id, params):
        return self._post("/charges/%s" % charge_id, params)

    def list(self, params=None):
        return self._get("/charges", params)

    def capture(self, charge_id):
        return self._post("/charges/%s/capture" % charge_id)

    def refund(self, charge_id, params=None):
        return self._post("/charges/%s/refund" % charge_id, params)
