from tests.integration.testcase import api, TestCase
from tests.integration import random_email, random_string


class TestCharges(TestCase):
    def test_create(self):
        email = random_email()
        customer = api.customers.create({
            'email': email
        })
        customer = api.customers.get(customer['id'])
        self.assertEqual(customer['email'], email)

        cardholder_name = random_string()
        card = api.cards.create(customer['id'], {
            'number': '4242424242424242',
            'expMonth': '12',
            'expYear': '2020',
            'cvc': '123',
            'cardholderName': cardholder_name
        })
        card = api.cards.get(card['customerId'], card['id'])
        self.assertEqual(card['last4'], '4242')
        self.assertEqual(card['expMonth'], '12')
        self.assertEqual(card['expYear'], '2020')
        self.assertEqual(card['cardholderName'], cardholder_name)

        charge = api.charges.create({
            'amount': 1000,
            'currency': 'EUR',
            'customerId': card['customerId']
        })
        charge = api.charges.get(charge['id'])
        self.assertEquals(charge['amount'], 1000)
        self.assertEquals(charge['currency'], 'EUR')
        self.assertEquals(charge['customerId'], card['customerId'])

    def test_create_twice(self):
        customer = api.customers.create({
            'email': random_email()
        })
        charge = api.charges.create({
            'amount': 2000,
            'currency': 'EUR',
            'customerId': customer['id'],
            'card': {
                'number': '4242424242424242',
                'expMonth': '12',
                'expYear': '2055',
                'cvc': '123'
            }
        })
        second_charge = api.charges.create({
            'amount': 1000,
            'currency': 'EUR',
            'customerId': charge['customerId']
        })
        self.assertEquals(second_charge['amount'], 1000)
        self.assertEquals(second_charge['customerId'], charge['customerId'])
