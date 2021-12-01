from tests.integration.testcase import api, TestCase
from tests.integration import random_email, random_string


class TestCards(TestCase):
    def test_create(self):
        customer = api.customers.create({"email": random_email()})
        cardholder_name = random_string()
        card = api.cards.create(
            customer["id"],
            {
                "number": "4242424242424242",
                "expMonth": "12",
                "expYear": "2055",
                "cvc": "123",
                "cardholderName": cardholder_name,
            },
        )
        card = api.cards.get(card["customerId"], card["id"])
        self.assertEqual(card["last4"], "4242")
        self.assertEqual(card["expMonth"], "12")
        self.assertEqual(card["expYear"], "2055")
        self.assertEqual(card["cardholderName"], cardholder_name)
