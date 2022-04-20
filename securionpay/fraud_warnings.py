from securionpay.resource import Resource


class FraudWarnings(Resource):
    def get(self, fraud_warning_id):
        return self._get("/fraud-warnings/%s" % fraud_warning_id)

    def list(self, params=None):
        return self._get("/fraud-warnings", params)
