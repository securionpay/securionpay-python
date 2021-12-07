from .data.credits import valid_credit_req
from .data.customers import valid_customer_req
from .testcase import api, TestCase


class TestCredits(TestCase):
    def test_create_and_get(self):
        # given
        credit_req = valid_credit_req()

        # when
        created = api.credits.create(credit_req)
        got = api.credits.get(created["id"])

        # then
        self.assertEqual(created, got)
        self.assertEqual(created["amount"], credit_req["amount"])
        self.assertEqual(created["currency"], credit_req["currency"])
        self.assertCardMatchesRequest(created["card"], credit_req["card"])

    def test_update(self):
        # given
        credit_req = valid_credit_req()
        created = api.credits.create(credit_req)

        # when
        updated = api.credits.update(
            created["id"],
            {
                "description": "updated description",
                "metadata": {"key": "updated value"},
            },
        )
        # then
        self.assertEqual(created["description"], credit_req["description"])
        self.assertEqual(updated["description"], "updated description")

        self.assertEqual(created["metadata"]["key"], credit_req["metadata"]["key"])
        self.assertEqual(updated["metadata"]["key"], "updated value")

        self.assertEqual(updated["amount"], credit_req["amount"])
        self.assertEqual(updated["currency"], credit_req["currency"])
        self.assertCardMatchesRequest(updated["card"], credit_req["card"])

    def test_list(self):
        # given
        customer = api.customers.create(valid_customer_req())
        credit_req = valid_credit_req(customerId=customer["id"])
        credit1 = api.credits.create(credit_req)
        credit2 = api.credits.create(credit_req)
        credit3 = api.credits.create(credit_req)

        # when
        all_credits = api.credits.list({"customerId": customer["id"]})
        credits_after_last_id = api.credits.list(
            {"customerId": customer["id"], "startingAfterId": credit3["id"]}
        )

        # then
        self.assertListResponseContainsExactlyById(
            all_credits, [credit3, credit2, credit1]
        )
        self.assertListResponseContainsExactlyById(
            credits_after_last_id, [credit2, credit1]
        )
