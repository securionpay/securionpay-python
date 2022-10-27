from securionpay.resource import Resource


class PaymentMethods(Resource):
    def create(self, params):
        return self._post("/payment-methods", params)

    def get(self, payment_method_id):
        return self._get("/payment-methods/%s" % payment_method_id)

    def delete(self, payment_method_id):
        return self._delete("/payment-methods/%s" % payment_method_id)

    def list(self, params=None):
        return self._get("/payment-methods", params)
