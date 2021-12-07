from .data.charges import valid_charge_req
from .data.customers import valid_customer_req
from .testcase import api, TestCase


class TestCharges(TestCase):
    def test_create_and_get(self):
        # given
        charge_req = valid_charge_req()

        # when
        created = api.charges.create(charge_req)
        got = api.charges.get(created["id"])

        # then
        self.assertEqual(created, got)
        self.assertEqual(created["amount"], charge_req["amount"])
        self.assertEqual(created["currency"], charge_req["currency"])
        self.assertCardMatchesRequest(created["card"], charge_req["card"])

    def test_update(self):
        # given
        charge_req = valid_charge_req()
        created = api.charges.create(charge_req)

        # when
        updated = api.charges.update(
            created["id"],
            {
                "description": "updated description",
                "metadata": {"key": "updated value"},
            },
        )
        # then
        self.assertEqual(created["description"], charge_req["description"])
        self.assertEqual(updated["description"], "updated description")

        self.assertEqual(created["metadata"]["key"], charge_req["metadata"]["key"])
        self.assertEqual(updated["metadata"]["key"], "updated value")

        self.assertEqual(updated["amount"], charge_req["amount"])
        self.assertEqual(updated["currency"], charge_req["currency"])
        self.assertCardMatchesRequest(updated["card"], charge_req["card"])

    def test_capture(self):
        # given
        charge_req = valid_charge_req(captured=False)
        created = api.charges.create(charge_req)

        # when
        captured = api.charges.capture(created["id"])

        # then
        self.assertFalse(created["captured"])
        self.assertTrue(captured["captured"])

    def test_refund(self):
        # given
        charge_req = valid_charge_req()
        created = api.charges.create(charge_req)

        # when
        refunded = api.charges.refund(created["id"])

        # then
        self.assertFalse(created["refunded"])
        self.assertTrue(refunded["refunded"])

    def test_list(self):
        # given
        customer = api.customers.create(valid_customer_req())
        charge_req = valid_charge_req(customerId=customer["id"])
        charge1 = api.charges.create(charge_req)
        charge2 = api.charges.create(charge_req)
        charge3 = api.charges.create(charge_req)

        # when
        all_charges = api.charges.list({"customerId": customer["id"]})
        charges_after_last_id = api.charges.list(
            {"customerId": customer["id"], "startingAfterId": charge3["id"]}
        )

        # then
        self.assertListResponseContainsExactlyById(
            all_charges, [charge3, charge2, charge1]
        )
        self.assertListResponseContainsExactlyById(
            charges_after_last_id, [charge2, charge1]
        )
