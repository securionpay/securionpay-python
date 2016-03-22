from securionpay.resource import Resource


class Charges(Resource):
    def create(self, params):
        return self.request('POST', [self.name()], params)

    def get(self, id):
        return self.request('GET', [self.name(), id])

    def update(self, id, params):
        return self.request('POST', [self.name(), id], params)

    def list(self, params=None):
        return self.request('GET', [self.name()], params)['list']

    def capture(self, charge_id):
        return self.request('POST', [self.name(), charge_id, 'capture'])

    def refund(self, charge_id, params=None):
        return self.request('POST', [self.name(), charge_id, 'refund'], params)
