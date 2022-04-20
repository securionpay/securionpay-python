from . import random_email
from .data.cards import valid_card_req
from .data.plans import one_week_plan_req
from .data.subscriptions import subscription_req
from .testcase import TestCase


class TestSubscriptions(TestCase):
    def test_create_and_get(self, api):
        # given
        customer = api.customers.create(
            {"email": random_email(), "card": valid_card_req()}
        )
        plan = api.plans.create(one_week_plan_req())

        # when
        created = api.subscriptions.create(
            subscription_req(customerId=customer["id"], planId=plan["id"])
        )
        got = api.subscriptions.get(created["id"])

        # then
        assert created["id"] is not None
        assert created == got
        assert created["customerId"] == customer["id"]
        assert created["planId"] == plan["id"]

    def test_update(self, api):
        # given
        customer = api.customers.create(
            {"email": random_email(), "card": valid_card_req()}
        )
        plan = api.plans.create(one_week_plan_req())
        created = api.subscriptions.create(
            subscription_req(customerId=customer["id"], planId=plan["id"])
        )
        # when
        api.subscriptions.update(
            created["id"],
            {
                "shipping": {
                    "name": "Updated shipping",
                    "address": {
                        "line1": "Updated line1",
                        "line2": "Updated line2",
                        "zip": "Updated zip",
                        "city": "Updated city",
                        "state": "Updated state",
                        "country": "CH",
                    },
                }
            },
        )
        updated = api.subscriptions.get(created["id"])

        # then
        assert "shipping" not in created
        assert updated["id"] == created["id"]
        assert updated["planId"] == plan["id"]

        shipping = updated["shipping"]
        assert shipping["name"] == "Updated shipping"
        assert shipping["address"]["line1"] == "Updated line1"
        assert shipping["address"]["line2"] == "Updated line2"
        assert shipping["address"]["zip"] == "Updated zip"
        assert shipping["address"]["city"] == "Updated city"
        assert shipping["address"]["state"] == "Updated state"
        assert shipping["address"]["country"] == "CH"


def find_charge_success(response):
    for event in response["list"]:
        if event["type"] == "CHARGE_SUCCEEDED":
            return event
