import unittest
import testcase

from securionpay import SecurionPayException


class TestCustomers(testcase.TestCase):
    def test_create(self):
        customer = self.gateway.customers.create({
            'email': 'user@example.com',
        })

    def test_create_without_email(self):
        with self.assertRaises(SecurionPayException):
            customer = self.gateway.customers.create({
            })

    def test_create_with_description(self):
        customer = self.gateway.customers.create({
            'email': 'user@example.com',
            'description': 'User description'
        })

    @unittest.skip("sth's wrong when creating user with card details")
    def test_create_with_card(self):
        customer = self.gateway.customers.create({
            'email': 'user@example.com',
            'description': 'User description',
            'card[number]': '4242424242424242',
            'card[expMonth]': '12',
            'card[expYear]': '2020',
            'card[cvc]': '123',
            'card[cardholderName]': 'John Smith'
        })

    def test_list(self):
        customers = self.gateway.customers.list()
        self.assertEquals(len(customers), 10)

    def test_get(self):
        customer = self.gateway.customers.get(self.gateway.customers.list()[0]['id'])

    def test_get_with_invalid_id(self):
        with self.assertRaises(SecurionPayException):
            customer = self.gateway.customers.get('1')
