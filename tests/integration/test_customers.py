from . import random_email
from .data.cards import valid_card_req
from .data.customers import valid_customer_req
from .testcase import TestCase


class TestCustomers(TestCase):
    def test_create_and_get(self, api):
        # given
        customer_req = valid_customer_req()
        # when
        created = api.customers.create(customer_req)
        got = api.customers.get(created["id"])
        # then
        assert created["id"] is not None
        assert created["email"] == customer_req["email"]
        assert got["email"] == customer_req["email"]

    def test_create_without_email(self, api):
        exception = self.assert_securion_pay_exception(api.customers.create, {})
        assert exception.type == "invalid_request"
        assert exception.code == None
        assert exception.message == "email: Must not be empty."
        assert exception.charge_id == None
        assert exception.blacklist_rule_id == None

    def test_get_with_invalid_id(self, api):
        exception = self.assert_securion_pay_exception(api.customers.get, "1")
        assert exception.type == "invalid_request"
        assert exception.code == None
        assert exception.message == "Customer '1' does not exist"
        assert exception.charge_id == None
        assert exception.blacklist_rule_id == None

    def test_delete(self, api):
        # given
        customer_req = valid_customer_req(card=valid_card_req())
        customer = api.customers.create(customer_req)

        # when
        api.customers.delete(customer["id"])
        deleted = api.customers.get(customer["id"])

        # then
        assert "deleted" not in customer
        assert deleted["deleted"]

    def test_update_default_card(self, api):
        # given
        customer_req = valid_customer_req(card=valid_card_req())
        customer = api.customers.create(customer_req)
        new_card = api.cards.create(customer["id"], valid_card_req())

        # when
        updated = api.customers.update(
            customer["id"], {"defaultCardId": new_card["id"]}
        )

        # then
        assert customer["defaultCardId"] != new_card["id"]
        assert updated["defaultCardId"] == new_card["id"]

    def test_list(self, api):
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
        self.assert_list_response_contains_exactly_by_id(
            all_customers, [customer2, customer1]
        )
        self.assert_list_response_contains_exactly_by_id(
            deleted_customers, [deleted_customer]
        )
