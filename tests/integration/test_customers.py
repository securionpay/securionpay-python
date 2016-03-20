import unittest
from securionpay import SecurionPayException, customers
from tests.integration import random_email


class TestCustomers(unittest.TestCase):
    def test_create(self):
        customers.create({
            'email': random_email()
        })

    def test_create_without_email(self):
        self.assertRaises(SecurionPayException, customers.create, {})

    def test_get_with_invalid_id(self):
        self.assertRaises(SecurionPayException, customers.get, '1')
