from . import random_email
from .data.cards import valid_card_req
from .data.plans import one_week_plan_req
from .testcase import api, TestCase


class TestTokens(TestCase):
    def test_create_and_get(self):
        # given
        token_req = valid_card_req()
        # when
        created = api.tokens.create(token_req)
        get = api.tokens.get(created["id"])
        # then
        self.assertEqual(get["last4"], token_req["number"][-4:])
        self.assertEqual(get["first6"], token_req["number"][:6])
        self.assertEqual(get["expMonth"], token_req["expMonth"])
        self.assertEqual(get["expYear"], token_req["expYear"])
        self.assertEqual(get["cardholderName"], token_req["cardholderName"])
        self.assertFalse(get["used"])

    def test_charge_via_token(self):
        # given
        token = api.tokens.create(valid_card_req())
        # when
        charge = api.charges.create(
            {"amount": 2000, "currency": "EUR", "card": token["id"], "captured": False}
        )
        charge = api.charges.capture(charge["id"])
        charge = api.charges.refund(charge["id"], {"amount": 1000})
        self.assertEqual(charge["amount"], 1000)
        self.assertTrue(charge["captured"])
        self.assertTrue(charge["refunded"])

    def test_subscribe_via_token(self):
        # given
        plan = api.plans.create(one_week_plan_req())
        customer = api.customers.create({"email": random_email()})
        token = api.tokens.create(valid_card_req())
        # when
        subscription = api.subscriptions.create(
            {"customerId": customer["id"], "planId": plan["id"], "card": token["id"]}
        )
        # then
        self.assertEqual(subscription["planId"], plan["id"])
        self.assertEqual(subscription["customerId"], customer["id"])
