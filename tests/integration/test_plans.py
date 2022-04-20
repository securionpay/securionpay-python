from .data.plans import one_week_plan_req
from .testcase import TestCase


class TestPlans(TestCase):
    def test_create_and_get(self, api):
        # given
        plan_req = one_week_plan_req()
        # when
        created = api.plans.create(plan_req)
        got = api.plans.get(created["id"])
        # then
        assert got["id"] == created["id"]
        assert got["amount"] == plan_req["amount"]
        assert got["currency"] == plan_req["currency"]
        assert got["interval"] == plan_req["interval"]
        assert got["name"] == plan_req["name"]

    def test_update(self, api):
        # given
        plan_req = one_week_plan_req()
        created = api.plans.create(plan_req)
        # when
        updated = api.plans.update(
            created["id"], {"amount": 222, "currency": "PLN", "name": "Updated plan"}
        )
        # then
        assert updated["id"] == created["id"]
        assert updated["interval"] == plan_req["interval"]
        assert updated["amount"] == 222
        assert updated["currency"] == "PLN"
        assert updated["name"] == "Updated plan"

    def test_delete(self, api):
        # given
        plan_req = one_week_plan_req()
        created = api.plans.create(plan_req)
        # when
        api.plans.delete(created["id"])
        updated = api.plans.get(created["id"])
        # then
        assert "deleted" not in created
        assert updated["deleted"]

    def test_list(self, api):
        # given
        plan1 = api.plans.create(one_week_plan_req())
        plan2 = api.plans.create(one_week_plan_req())
        deleted_plan = api.plans.create(one_week_plan_req())
        api.plans.delete(deleted_plan["id"])
        # when
        all_plans = api.plans.list({"limit": 100})
        deleted_plans = api.plans.list({"limit": 100, "deleted": True})

        # then
        self.assertListResponseContainsInAnyOrderById(all_plans, [plan2, plan1])
        self.assertListResponseContainsInAnyOrderById(deleted_plans, [deleted_plan])
