import unittest
from securionpay import customers, cards


class TestCards(unittest.TestCase):
    def test_create(self):
        resp = cards.create(customers.list()[0]['id'], {
            'number': '4242424242424242',
            'expMonth': '12',
            'expYear': '2020',
            'cvc': '123',
            'cardholderName': 'John Smith'
        })

    def test_list(self):
        resp = cards.list(customers.list()[0]['id'])
        self.assertEquals(len(resp), 1)
