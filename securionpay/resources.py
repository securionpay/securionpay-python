from securionpay.request import request, create_url


class Resource(object):
    def name(self):
        return self.__class__.__name__.lower()

    def url(self):
        return create_url([self.name()])

    def instance_url(self, id, parts=[]):
        return create_url([self.name(), id] + parts)


class CreateableResource(Resource):
    def create(self, params):
        return request('POST', self.url(), params)


class GettableResource(Resource):
    def get(self, id):
        return request('GET', self.instance_url(id), None)


class UpdateableResource(Resource):
    def update(self, id, params):
        return request('POST', self.instance_url(id), params)


class DeleteableResource(Resource):
    def delete(self, id):
        return request('DELETE', self.instance_url(id), None)


class ListableResource(Resource):
    def list(self, params=None):
        return request('GET', self.url(), params)['list']


class Customers(GettableResource,
                CreateableResource,
                UpdateableResource,
                DeleteableResource,
                ListableResource):
    pass


class Charges(GettableResource,
              CreateableResource,
              UpdateableResource,
              ListableResource):

    def capture(self, charge_id):
        return request('POST', self.instance_url(charge_id, ['capture']), None)

    def refund(self, charge_id, params=None):
        return request('POST', self.instance_url(charge_id, ['refund']), params)
