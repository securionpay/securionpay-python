from securionpay.resource import Resource


class Events(Resource):
    def get(self, event_id):
        return self._get("/events/%s" % event_id)

    def list(self, params=None):
        return self._get("/events", params)
