import unittest
import securionpay as api
from tests.integration import random_email, random_string


class TestCharges(unittest.TestCase):
    def test_create(self):
        email = random_email()
        customer = api.customers.create({
            'email': email
        })
        customer = api.customers.get(customer['id'])
        self.assertEqual(customer['email'], email)

        cardholderName = random_string()
        card = api.cards.create(customer['id'], {
            'number': '4242424242424242',
            'expMonth': '12',
            'expYear': '2020',
            'cvc': '123',
            'cardholderName': cardholderName
        })
        card = api.cards.get(card['customerId'], card['id'])
        self.assertEqual(card['last4'], '4242')
        self.assertEqual(card['expMonth'], '12')
        self.assertEqual(card['expYear'], '2020')
        self.assertEqual(card['cardholderName'], cardholderName)

        charge = api.charges.create({
            'amount': 1000,
            'currency': 'EUR',
            'customerId': card['customerId']
        })
        charge = api.charges.get(charge['id'])
        self.assertEquals(charge['amount'], 1000)
        self.assertEquals(charge['currency'], 'EUR')
        self.assertEquals(charge['customerId'], card['customerId'])