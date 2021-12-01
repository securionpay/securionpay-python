from securionpay.resource import Resource


class Subscriptions(Resource):
    def create(self, params):
        return self._post("/subscriptions", params)

    def get(self, subscription_id):
        return self._get("/subscriptions/%s" % subscription_id)

    def update(self, subscription_id, params):
        return self._post("/subscriptions/%s" % subscription_id, params)

    def cancel(self, subscription_id):
        return self._delete("/subscriptions/%s" % subscription_id)

    def list(self, params=None):
        return self._get("/subscriptions", params)
