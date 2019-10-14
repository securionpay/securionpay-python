from tests.integration.testcase import api, TestCase
from tests.integration import random_email, random_string


class TestTokens(TestCase):
    def test_charge_capture_refund_via_token(self):
        cardholder_name = random_string()
        token = api.tokens.create(
            {
                "number": "4242424242424242",
                "expMonth": "12",
                "expYear": "2055",
                "cvc": "123",
                "cardholderName": cardholder_name,
            }
        )
        charge = api.charges.create(
            {"amount": 2000, "currency": "EUR", "card": token["id"], "captured": False}
        )
        charge = api.charges.capture(charge["id"])
        charge = api.charges.refund(charge["id"], {"amount": 1000})
        self.assertEqual(charge["amount"], 2000)
        self.assertEqual(charge["amountRefunded"], 1000)
        self.assertEqual(charge["captured"], True)
        self.assertEqual(charge["refunded"], True)

    def test_subscribe_via_token(self):
        plan = api.plans.create(
            {
                "amount": 1000,
                "currency": "EUR",
                "interval": "month",
                "name": random_string(),
            }
        )
        customer = api.customers.create({"email": random_email()})
        token = api.tokens.create(
            {
                "number": "4242424242424242",
                "expMonth": "12",
                "expYear": "2055",
                "cvc": "123",
            }
        )
        subscription = api.subscriptions.create(
            customer["id"], {"planId": plan["id"], "card": token["id"]}
        )
        self.assertEqual(subscription["planId"], plan["id"])
        self.assertEqual(subscription["customerId"], customer["id"])
