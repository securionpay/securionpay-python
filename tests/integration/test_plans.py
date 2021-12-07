from .data.plans import one_week_plan_req
from .testcase import api, TestCase


class TestPlans(TestCase):
    def test_create_and_get(self):
        # given
        plan_req = one_week_plan_req()
        # when
        created = api.plans.create(plan_req)
        got = api.plans.get(created["id"])
        # then
        self.assertEqual(got["id"], created["id"])
        self.assertEqual(got["amount"], plan_req["amount"])
        self.assertEqual(got["currency"], plan_req["currency"])
        self.assertEqual(got["interval"], plan_req["interval"])
        self.assertEqual(got["name"], plan_req["name"])

    def test_update(self):
        # given
        plan_req = one_week_plan_req()
        created = api.plans.create(plan_req)
        # when
        updated = api.plans.update(
            created["id"], {"amount": 222, "currency": "PLN", "name": "Updated plan"}
        )
        # then
        self.assertEqual(updated["id"], created["id"])
        self.assertEqual(updated["interval"], plan_req["interval"])
        self.assertEqual(updated["amount"], 222)
        self.assertEqual(updated["currency"], "PLN")
        self.assertEqual(updated["name"], "Updated plan")

    def test_delete(self):
        # given
        plan_req = one_week_plan_req()
        created = api.plans.create(plan_req)
        # when
        api.plans.delete(created["id"])
        updated = api.plans.get(created["id"])
        # then
        self.assertNotIn("deleted", created)
        self.assertTrue(updated["deleted"])

    def test_list(self):
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
