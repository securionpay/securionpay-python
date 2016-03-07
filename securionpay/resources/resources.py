import requests
from securionpay import SecurionPayException

api_url = "https://api.securionpay.com"


def create_url(parts):
    return "/".join([api_url] + parts)


class Resources(object):
    def __init__(self, auth, obj):
        self.auth = auth
        self.obj = obj

    def request(self, method, parts, params = None):
        resp = getattr(requests, method)(create_url(parts), json=params, auth=self.auth)
        if resp.status_code == 200:
            return resp.json()
        raise SecurionPayException('Server response status code: %d (%s)\nRequest parts: %s\nParams: %s' %
                        (resp.status_code, resp.reason, str(parts), str(params)))

    def create(self, params):
        return self.request('post', [self.obj], params)

    def get(self, id):
        return self.request('get', [self.obj, id])

    def update(self, id, params):
        return self.request('post', [self.obj, id], params)

    def delete(self, id):
        return self.request('delete', [self.obj, id])

    def list(self):
        return self.request('get', [self.obj])['list']


class Cards(Resources):
    def __init__(self, auth):
        super(Cards, self).__init__(auth, 'cards')

    def create(self, customer_id, params):
        return super(Cards, self).request('post', ['customers', customer_id, self.obj], params)

    def get(self, customer_id, card_id):
        return super(Cards, self).request('get', ['customers', customer_id, self.obj, card_id])

    def list(self, customer_id):
        return super(Cards, self).request('get', ['customers', customer_id, self.obj])['list']


class Customers(Resources):
    def __init__(self, auth):
        super(Customers, self).__init__(auth, 'customers')

