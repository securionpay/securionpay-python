from securionpay.resource import Resource


class Cards(Resource):
    def create(self, customer_id, params):
        return self.request('POST', ['customers', customer_id, self.name()], params)

    def get(self, customer_id, id):
        return self.request('GET', ['customers', customer_id, self.name(), id])

    def update(self, customer_id, id, params):
        return self.request('POST', ['customers', customer_id, self.name(), id], params)

    def delete(self, customer_id, id):
        return self.request('DELETE', ['customers', customer_id, self.name(), id])

    def list(self, customer_id, params=None):
        return self.request('GET', ['customers', customer_id, self.name()], params)['list']
