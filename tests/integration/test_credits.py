from .data.credits import valid_credit_req
from .data.customers import valid_customer_req
from .testcase import TestCase


class TestCredits(TestCase):
    def test_create_and_get(self, api):
        # given
        credit_req = valid_credit_req()

        # when
        created = api.credits.create(credit_req)
        got = api.credits.get(created["id"])

        # then
        assert created == got
        assert created["amount"] == credit_req["amount"]
        assert created["currency"] == credit_req["currency"]
        self.assert_card_matches_request(created["card"], credit_req["card"])

    def test_update(self, api):
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
        assert created["description"] == credit_req["description"]
        assert updated["description"] == "updated description"

        assert created["metadata"]["key"] == credit_req["metadata"]["key"]
        assert updated["metadata"]["key"] == "updated value"

        assert updated["amount"] == credit_req["amount"]
        assert updated["currency"] == credit_req["currency"]
        self.assert_card_matches_request(updated["card"], credit_req["card"])

    def test_list(self, api):
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
        self.assert_list_response_contains_exactly_by_id(
            all_credits, [credit3, credit2, credit1]
        )
        self.assert_list_response_contains_exactly_by_id(
            credits_after_last_id, [credit2, credit1]
        )
