from securionpay.resource import Resource


class Customers(Resource):
    def create(self, params):
        return self.request('POST', [self.name()], params)

    def get(self, id):
        return self.request('GET', [self.name(), id])

    def update(self, id, params):
        return self.request('POST', [self.name(), id], params)

    def delete(self, id):
        return self.request('DELETE', [self.name(), id])

    def list(self, params=None):
        return self.request('GET', [self.name()], params)['list']
