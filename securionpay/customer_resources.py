from securionpay.request import request, create_url


class CustomerResource(object):
    def name(self):
        return self.__class__.__name__.lower()

    def url(self, customer_id):
        return create_url(['customers', customer_id, self.name()])

    def instance_url(self, customer_id, id, parts=[]):
        return create_url(['customers', customer_id, self.name(), id] + parts)


class CustomerCreateableResource(CustomerResource):
    def create(self, customer_id, params):
        return request('POST', self.url(customer_id), params)


class CustomerGettableResource(CustomerResource):
    def get(self, customer_id, id):
        return request('GET', self.instance_url(customer_id, id), None)


class CustomerUpdateableResource(CustomerResource):
    def update(self, customer_id, id, params):
        return request('POST', self.instance_url(customer_id, id), params)


class CustomerDeleteableResource(CustomerResource):
    def delete(self, customer_id, id):
        return request('DELETE', self.instance_url(customer_id, id), None)


class CustomerListableResource(CustomerResource):
    def list(self, customer_id, params=None):
        return request('GET', self.url(customer_id), params)['list']


class Cards(CustomerCreateableResource,
            CustomerGettableResource,
            CustomerUpdateableResource,
            CustomerDeleteableResource,
            CustomerListableResource):
    pass
