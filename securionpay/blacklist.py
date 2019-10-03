from securionpay.resource import Resource


class Blacklist(Resource):
    def create(self, params):
        return self._post("/blacklist", params)

    def get(self, blacklist_rule_id):
        return self._get("/blacklist/%s" % blacklist_rule_id)

    def delete(self, blacklist_rule_id):
        return self._delete("/blacklist/%s" % blacklist_rule_id)

    def list(self, params=None):
        return self._get("/blacklist", params)
