from . import random_email
from .data.cards import valid_card_req
from .data.plans import one_week_plan_req
from .data.subscriptions import subscription_req
from .testcase import api, TestCase


class TestSubscriptions(TestCase):
    def test_create_and_get(self):
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
        self.assertIsNotNone(created["id"])
        self.assertEqual(created, got)
        self.assertEqual(created["customerId"], customer["id"])
        self.assertEqual(created["planId"], plan["id"])

    def test_update(self):
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
        self.assertNotIn("shipping", created)
        self.assertEqual(updated["id"], created["id"])
        self.assertEqual(updated["planId"], plan["id"])

        shipping = updated["shipping"]
        self.assertEqual(shipping["name"], "Updated shipping")
        self.assertEqual(shipping["address"]["line1"], "Updated line1")
        self.assertEqual(shipping["address"]["line2"], "Updated line2")
        self.assertEqual(shipping["address"]["zip"], "Updated zip")
        self.assertEqual(shipping["address"]["city"], "Updated city")
        self.assertEqual(shipping["address"]["state"], "Updated state")
        self.assertEqual(shipping["address"]["country"], "CH")


def find_charge_success(response):
    for event in response["list"]:
        if event["type"] == "CHARGE_SUCCEEDED":
            return event
