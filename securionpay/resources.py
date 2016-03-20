from securionpay.request import request


def create_url(parts):
    return "/".join([str(part) for part in parts])


class Resources(object):
    def __init__(self, obj):
        self.obj = obj

    def request(self, method, parts, params=None):
        return request(method, create_url([self.obj] + parts), params)

    def create(self, params):
        return self.request('post', [], params)

    def get(self, id):
        return self.request('get', [id])

    def update(self, id, params):
        return self.request('post', [id], params)

    def delete(self, id):
        return self.request('delete', [id])

    def list(self, params=None):
        return self.request('get', [], params)['list']


class CustomerSubresource(object):
    def __init__(self, obj):
        self.obj = obj

    def request(self, method, customer_id, parts, params=None):
        return request(method, create_url(['customers', customer_id, self.obj] + parts), params)

    def create(self, customer_id, params):
        return self.request('post', customer_id, [], params)

    def get(self, customer_id, id):
        return self.request('get', customer_id, [id])

    def update(self, customer_id, id, params):
        return self.request('post', customer_id, [id], params)

    def delete(self, customer_id, id):
        return self.request('delete', customer_id, [id])

    def list(self, customer_id, params=None):
        return self.request('get', customer_id, [], params)['list']


class Cards(CustomerSubresource):
    def __init__(self):
        super(Cards, self).__init__('cards')


class Customers(Resources):
    def __init__(self):
        super(Customers, self).__init__('customers')


class Charges(Resources):
    def __init__(self):
        super(Charges, self).__init__('charges')

    def capture(self, charge_id):
        return self.request('post', [charge_id, 'capture'])

    def refund(self, charge_id, params=None):
        return self.request('post', [charge_id, 'refund'], params)
