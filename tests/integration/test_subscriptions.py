from tests.integration import random_email
from tests.integration.data.cards import valid_card_req
from tests.integration.data.plans import one_week_plan_req
from tests.integration.data.subscriptions import subscription_req
from tests.integration.testcase import api, TestCase


class TestSubscriptions(TestCase):
    def test_create(self):
        # given
        customer = api.customers.create({"email": random_email(), "card": valid_card_req()})
        plan = api.plans.create(one_week_plan_req())

        # when
        subscription = api.subscriptions.create(subscription_req(customer["id"], plan["id"]))

        # then
        charge = api.charges.list()["list"][0]
        self.assertEqual(charge["subscriptionId"], subscription["id"])

        event = find_charge_success(api.events.list())
        self.assertEqual(event["data"]["objectType"], 'charge')
        self.assertEqual(event["data"]["subscriptionId"], subscription["id"])


def find_charge_success(response):
    for event in response["list"]:
        if event["type"] == 'CHARGE_SUCCEEDED':
            return event
