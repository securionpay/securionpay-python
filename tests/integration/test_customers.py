from tests.integration.testcase import api, TestCase
from tests.integration import random_email


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
