from .data.charges import valid_charge_req
from .testcase import api, TestCase


def create_event():
    charge = api.charges.create(valid_charge_req())
    events = api.events.list({"limit": 100})
    for event in events["list"]:
        if event.get("data", {}).get("id") == charge["id"]:
            return [event, charge]
    raise AssertionError("Expected event not created")


class TestDisputes(TestCase):
    def test_get(self):
        # given
        [event, charge] = create_event()
        # when
        retrieved = api.events.get(event["id"])
        # then
        self.assertEqual(retrieved["data"]["id"], charge["id"])

    def test_list(self):
        # given
        [event, _] = create_event()
        # when
        response = api.events.list({"limit": 100})
        # then
        self.assertListResponseContainsInAnyOrderById(response, [event])
