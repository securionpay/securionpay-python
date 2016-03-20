from tests.integration.testcase import api, TestCase
from tests.integration import random_email


class TestCustomers(TestCase):
    def test_create(self):
        api.customers.create({
            'email': random_email()
        })

    def test_create_without_email(self):
        self.assertRaises(api.SecurionPayException, api.customers.create, {})

    def test_get_with_invalid_id(self):
        self.assertRaises(api.SecurionPayException, api.customers.get, '1')
