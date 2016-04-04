from securionpay.resource import Resource


class CustomerRecords(Resource):
    def buy(self, params):
        return self._post('/customer-records', params)

    def refresh(self, customer_record_id, params=None):
        return self._post('/customer-records/%s' % customer_record_id, params)

    def get(self, customer_record_id):
        return self._get('/customer-records/%s' % customer_record_id)

    def list(self, params=None):
        return self._get('/customer-records', params)['list']

    def get_fee(self, customer_record_id, customer_record_fee_id):
        return self._get('/customer-records/%s/fees/%s' % (customer_record_id, customer_record_fee_id))

    def list_fees(self, customer_record_id, params=None):
        return self._get('/customer-records/%s/fees' % customer_record_id, params)['list']

    def get_profit(self, customer_record_id, customer_record_profit_id):
        return self._get('/customer-records/%s/profits/%s' % (customer_record_id, customer_record_profit_id))

    def list_profits(self, customer_record_id, params=None):
        return self._get('/customer-records/%s/profits' % customer_record_id, params)['list']
