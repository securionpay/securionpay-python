import unittest
from securionpay import SecurionPayException, customers


class TestCustomers(unittest.TestCase):
    def test_create(self):
        resp = customers.create({
            'email': 'user@example.com',
        })

    def test_create_without_email(self):
        with self.assertRaises(SecurionPayException):
            resp = customers.create({
            })

    def test_create_with_description(self):
        resp = customers.create({
            'email': 'user@example.com',
            'description': 'User description'
        })

    @unittest.skip("sth's wrong when creating user with card details")
    def test_create_with_card(self):
        resp = customers.create({
            'email': 'user@example.com',
            'description': 'User description',
            'card[number]': '4242424242424242',
            'card[expMonth]': '12',
            'card[expYear]': '2020',
            'card[cvc]': '123',
            'card[cardholderName]': 'John Smith'
        })

    def test_list(self):
        resp = customers.list()
        self.assertEquals(len(resp), 10)

    def test_get(self):
        resp = customers.get(customers.list()[0]['id'])

    def test_get_with_invalid_id(self):
        with self.assertRaises(SecurionPayException):
            resp = customers.get('1')
