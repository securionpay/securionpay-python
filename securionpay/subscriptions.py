from securionpay.resource import Resource


class Subscriptions(Resource):
    def path(self, customer_id, subscription_id=None):
        path = '/customers/%s/subscriptions' % customer_id
        if subscription_id:
            path += '/%s' % subscription_id
        return path

    def create(self, customer_id, params):
        return self._post(self.path(customer_id), params)

    def get(self, customer_id, subscription_id):
        return self._get(self.path(customer_id, subscription_id))

    def update(self, customer_id, subscription_id, params):
        return self._post(self.path(customer_id, subscription_id), params)

    def cancel(self, customer_id, subscription_id):
        return self._delete(self.path(customer_id, subscription_id))

    def list(self, customer_id, params=None):
        return self._get(self.path(customer_id), params)
