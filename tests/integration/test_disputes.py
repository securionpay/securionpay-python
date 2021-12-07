from waiting import wait

from .data.cards import disputed_card_req
from .data.charges import valid_charge_req
from .testcase import api, TestCase


def create_dispute():
    charge = api.charges.create(valid_charge_req(card=disputed_card_req()))
    wait(
        lambda: api.charges.get(charge["id"]).get("disputed") is True,
        timeout_seconds=30,
    )
    disputes = api.disputes.list({"limit": 100})
    for dispute in disputes["list"]:
        if dispute.get("charge", {}).get("id") == charge["id"]:
            return [dispute, charge]
    raise AssertionError("Expected dispute to be created")


class TestDisputes(TestCase):
    def test_get(self):
        # given
        [dispute, charge] = create_dispute()
        # when
        retrieved = api.disputes.get(dispute["id"])
        # then
        self.assertEqual(retrieved["charge"]["id"], charge["id"])

    def test_update(self):
        # given
        [dispute, _] = create_dispute()
        evidence_customer_name = "Test Customer"
        # when
        api.disputes.update(
            dispute["id"], {"evidence": {"customerName": evidence_customer_name}}
        )
        updated = api.disputes.get(dispute["id"])
        # then
        self.assertEqual(updated["evidence"]["customerName"], evidence_customer_name)

    def test_close(self):
        # given
        [dispute, _] = create_dispute()
        # when
        api.disputes.close(dispute["id"])
        closed = api.disputes.get(dispute["id"])
        # then
        self.assertTrue(closed["acceptedAsLost"])

    def test_list(self):
        # given
        [dispute, _] = create_dispute()
        # when
        response = api.disputes.list({"limit": 100})
        # then
        self.assertListResponseContainsInAnyOrderById(response, [dispute])
