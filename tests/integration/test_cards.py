from . import random_email, random_string
from .data.cards import valid_card_req
from .testcase import TestCase


class TestCards(TestCase):
    def test_create_and_get(self, api):
        # given
        customer = api.customers.create({"email": random_email()})
        card_req = {
            "number": "4242424242424242",
            "expMonth": "12",
            "expYear": "2055",
            "cvc": "123",
            "cardholderName": (random_string()),
        }

        # when
        created = api.cards.create(
            customer["id"],
            card_req,
        )
        retrieved = api.cards.get(created["customerId"], created["id"])

        # then
        self.assert_card_matches_request(created, card_req)
        assert created == retrieved

    def test_update(self, api):
        # given
        customer = api.customers.create({"email": random_email()})
        created = api.cards.create(customer["id"], valid_card_req())

        # when
        update_request = {
            "expMonth": "05",
            "expYear": "2055",
            "cardholderName": "updated cardholderName",
            "addressCountry": "updated addressCountry",
            "addressCity": "updated addressCity",
            "addressState": "updated addressState",
            "addressZip": "updated addressZip",
            "addressLine1": "updated addressLine1",
            "addressLine2": "updated addressLine2",
        }
        updated = api.cards.update(created["customerId"], created["id"], update_request)

        # then
        expected = dict()
        expected.update(created)
        expected.update(update_request)
        assert updated == expected

    def test_delete(self, api):
        # given
        customer = api.customers.create({"email": random_email()})
        created = api.cards.create(customer["id"], valid_card_req())

        # when
        api.cards.delete(created["customerId"], created["id"])
        deleted = api.cards.get(created["customerId"], created["id"])

        # then
        assert "deleted" not in created
        assert deleted["deleted"]

    def test_list(self, api):
        # given
        customer1 = api.customers.create({"email": random_email()})
        customer2 = api.customers.create({"email": random_email()})

        card11 = api.cards.create(customer1["id"], valid_card_req())
        card12 = api.cards.create(customer1["id"], valid_card_req())
        card21 = api.cards.create(customer2["id"], valid_card_req())

        # when
        customer1_cards = api.cards.list(customer1["id"])
        customer1_cards_limit1 = api.cards.list(customer1["id"], {"limit": 1})
        customer2_cards = api.cards.list(customer2["id"], {"limit": 1})

        # then
        self.assert_list_response_contains_exactly_by_id(
            customer1_cards, [card12, card11]
        )
        self.assert_list_response_contains_exactly_by_id(
            customer1_cards_limit1, [card12]
        )
        self.assert_list_response_contains_exactly_by_id(customer2_cards, [card21])
