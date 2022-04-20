from waiting import wait

from .data.cards import disputed_card_req
from .data.charges import valid_charge_req
from .testcase import TestCase


def create_dispute(api):
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
    def test_get(self, api):
        # given
        [dispute, charge] = create_dispute(api)
        # when
        retrieved = api.disputes.get(dispute["id"])
        # then
        assert retrieved["charge"]["id"] == charge["id"]

    def test_update(self, api):
        # given
        [dispute, _] = create_dispute(api)
        evidence_customer_name = "Test Customer"
        # when
        api.disputes.update(
            dispute["id"], {"evidence": {"customerName": evidence_customer_name}}
        )
        updated = api.disputes.get(dispute["id"])
        # then
        assert updated["evidence"]["customerName"] == evidence_customer_name

    def test_close(self, api):
        # given
        [dispute, _] = create_dispute(api)
        # when
        api.disputes.close(dispute["id"])
        closed = api.disputes.get(dispute["id"])
        # then
        assert closed["acceptedAsLost"]

    def test_list(self, api):
        # given
        [dispute, _] = create_dispute(api)
        # when
        response = api.disputes.list({"limit": 100})
        # then
        self.assertListResponseContainsInAnyOrderById(response, [dispute])
