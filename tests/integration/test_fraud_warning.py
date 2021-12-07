from waiting import wait

from .data.cards import fraud_warning_card_req
from .data.charges import valid_charge_req
from .testcase import api, TestCase


def create_fraud_warning():
    charge = api.charges.create(valid_charge_req(card=fraud_warning_card_req()))
    # fmt: off
    wait(
        lambda: api.charges.get(charge["id"])["fraudDetails"]["status"] != "in_progress",
        timeout_seconds=30,
        expected_exceptions=KeyError,
    )
    # fmt: on
    fraud_warnings = api.fraud_warnings.list({"limit": 100})
    for fraud_warning in fraud_warnings["list"]:
        if fraud_warning.get("charge") == charge["id"]:
            return [fraud_warning, charge]
    raise AssertionError("Expected fraud_warning to be created")


class TestFraudWarning(TestCase):
    def test_get(self):
        # given
        [fraud_warning, charge] = create_fraud_warning()
        # when
        retrieved = api.fraud_warnings.get(fraud_warning["id"])
        # then
        self.assertEqual(retrieved["charge"], charge["id"])

    def test_list(self):
        # given
        [fraud_warning, _] = create_fraud_warning()
        # when
        response = api.fraud_warnings.list({"limit": 100})
        # then
        self.assertListResponseContainsInAnyOrderById(response, [fraud_warning])
