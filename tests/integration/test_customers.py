from tests.integration.testcase import api, TestCase
from tests.integration import random_email, random_string


class TestCustomers(TestCase):
    def test_create(self):
        api.customers.create({
            'email': random_email()
        })

    def test_create_without_email(self):
        exception = self.assertSecurionPayException(api.customers.create, {})
        self.assertEqual(exception.type, "invalid_request")
        self.assertEqual(exception.code, None)
        self.assertEqual(exception.message, "email: may not be empty")
        self.assertEqual(exception.charge_id, None)
        self.assertEqual(exception.blacklist_rule_id, None)

    def test_get_with_invalid_id(self):
        exception = self.assertSecurionPayException(api.customers.get, '1')
        self.assertEqual(exception.type, "invalid_request")
        self.assertEqual(exception.code, None)
        self.assertEqual(exception.message, "Requested Customer does not exist")
        self.assertEqual(exception.charge_id, None)
        self.assertEqual(exception.blacklist_rule_id, None)

    def customer_from_charge(self):
        token = api.tokens.create({
            'number': '4242424242424242',
            'expMonth': '12',
            'expYear': '2055',
            'cvc': '123',
            'cardholderName': random_string()
        })
        charge = api.charges.create({
            'amount': 2000,
            'currency': 'EUR',
            'card': token['id']
        })
        customer = api.customers.create({
            'email': random_email(),
            'card': charge['id']
        })
        charge = api.charges.create({
            'amount': 1000,
            'currency': 'USD',
            'customerId': customer['id']
        })
        self.assertEquals(charge['amount'], 1000)
        self.assertEquals(charge['customerId'], customer['id'])
