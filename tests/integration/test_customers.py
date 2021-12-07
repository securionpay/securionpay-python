from . import random_email
from .data.cards import valid_card_req
from .data.customers import valid_customer_req
from .testcase import api, TestCase


class TestCustomers(TestCase):
    def test_create_and_get(self):
        # given
        customer_req = valid_customer_req()
        # when
        created = api.customers.create(customer_req)
        got = api.customers.get(created["id"])
        # then
        self.assertIsNotNone(created["id"])
        self.assertEqual(created["email"], customer_req["email"])
        self.assertEqual(got["email"], customer_req["email"])

    def test_create_without_email(self):
        exception = self.assertSecurionPayException(api.customers.create, {})
        self.assertEqual(exception.type, "invalid_request")
        self.assertEqual(exception.code, None)
        self.assertEqual(exception.message, "email: Must not be empty.")
        self.assertEqual(exception.charge_id, None)
        self.assertEqual(exception.blacklist_rule_id, None)

    def test_get_with_invalid_id(self):
        exception = self.assertSecurionPayException(api.customers.get, "1")
        self.assertEqual(exception.type, "invalid_request")
        self.assertEqual(exception.code, None)
        self.assertEqual(exception.message, "Customer '1' does not exist")
        self.assertEqual(exception.charge_id, None)
        self.assertEqual(exception.blacklist_rule_id, None)

    def test_delete(self):
        # given
        customer_req = valid_customer_req(card=valid_card_req())
        customer = api.customers.create(customer_req)

        # when
        api.customers.delete(customer["id"])
        deleted = api.customers.get(customer["id"])

        # then
        self.assertNotIn("deleted", customer)
        self.assertTrue(deleted["deleted"])

    def test_update_default_card(self):
        # given
        customer_req = valid_customer_req(card=valid_card_req())
        customer = api.customers.create(customer_req)
        new_card = api.cards.create(customer["id"], valid_card_req())

        # when
        updated = api.customers.update(
            customer["id"], {"defaultCardId": new_card["id"]}
        )

        # then
        self.assertNotEqual(customer["defaultCardId"], new_card["id"])
        self.assertEqual(updated["defaultCardId"], new_card["id"])

    def test_list(self):
        # given
        email = random_email()
        customer_req = valid_customer_req(email=email)
        customer1 = api.customers.create(customer_req)
        customer2 = api.customers.create(customer_req)
        deleted_customer = api.customers.create(customer_req)
        api.customers.delete(deleted_customer["id"])

        # when
        all_customers = api.customers.list({"email": email})
        deleted_customers = api.customers.list({"email": email, "deleted": True})

        # then
        self.assertListResponseContainsExactlyById(
            all_customers, [customer2, customer1]
        )
        self.assertListResponseContainsExactlyById(
            deleted_customers, [deleted_customer]
        )
