from securionpay.resource import Resource


class Customers(Resource):
    def create(self, params):
        return self._post("/customers", params)

    def get(self, customer_id):
        return self._get("/customers/%s" % customer_id)

    def update(self, customer_id, params):
        return self._post("/customers/%s" % customer_id, params)

    def delete(self, customer_id):
        return self._delete("/customers/%s" % customer_id)

    def list(self, params=None):
        return self._get("/customers", params)
