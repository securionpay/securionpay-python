import unittest
from securionpay import customers, cards
from tests.integration import random_email, random_string


class TestCards(unittest.TestCase):
    def test_create(self):
        customer = customers.create({
            'email': random_email()
        })
        resp = cards.create(customer['id'], {
            'number': '4242424242424242',
            'expMonth': '12',
            'expYear': '2020',
            'cvc': '123',
            'cardholderName': random_string()
        })
