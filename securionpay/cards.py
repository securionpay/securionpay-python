from securionpay.resource import Resource


class Cards(Resource):
    def path(self, customer_id, card_id=None):
        path = '/customers/%s/cards' % customer_id
        if card_id:
            path += '/%s' % card_id
        return path

    def create(self, customer_id, params):
        return self._post(self.path(customer_id), params)

    def get(self, customer_id, card_id):
        return self._get(self.path(customer_id, card_id))

    def update(self, customer_id, card_id, params):
        return self._post(self.path(customer_id, card_id), params)

    def delete(self, customer_id, card_id):
        return self._delete(self.path(customer_id, card_id))

    def list(self, customer_id, params=None):
        return self._get(self.path(customer_id), params)['list']
