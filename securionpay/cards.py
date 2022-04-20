from securionpay.resource import Resource


class Cards(Resource):
    def create(self, customer_id, params):
        return self._post("/customers/%s/cards" % customer_id, params)

    def get(self, customer_id, card_id):
        return self._get("/customers/%s/cards/%s" % (customer_id, card_id))

    def update(self, customer_id, card_id, params):
        return self._post("/customers/%s/cards/%s" % (customer_id, card_id), params)

    def delete(self, customer_id, card_id):
        return self._delete("/customers/%s/cards/%s" % (customer_id, card_id))

    def list(self, customer_id, params=None):
        return self._get("/customers/%s/cards" % customer_id, params)
