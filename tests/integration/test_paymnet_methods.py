from .data.customers import valid_customer_req
from .data.payment_methods import payment_method
from .testcase import TestCase


class TestPlans(TestCase):
    def test_create_and_get(self, api):
        # given
        payment_method_req = payment_method()
        # when
        created = api.payment_methods.create(payment_method_req)
        got = api.payment_methods.get(created["id"])
        # then
        assert got["id"] == created["id"]
        assert got["clientObjectId"] == created["clientObjectId"]
        assert got["type"] == payment_method_req["type"]
        assert got["billing"] == payment_method_req["billing"]
        assert got["status"] == "chargeable"

    def test_delete(self, api):
        # given
        payment_method_req = payment_method()
        created = api.payment_methods.create(payment_method_req)
        # when
        api.payment_methods.delete(created["id"])
        updated = api.payment_methods.get(created["id"])
        # then
        assert "deleted" not in created
        assert updated["deleted"]

    def test_list(self, api):
        # given
        customer = api.customers.create(valid_customer_req())
        payment_method_req = payment_method(customerId=customer["id"])
        payment_method1 = api.payment_methods.create(payment_method_req)
        payment_method2 = api.payment_methods.create(payment_method_req)
        payment_method3 = api.payment_methods.create(payment_method_req)
        # when
        all_payment_methods = api.payment_methods.list({"customerId": customer["id"]})
        payment_methods_after_last_id = api.payment_methods.list(
            {"customerId": customer["id"], "startingAfterId": payment_method3["id"]}
        )
        # then
        self.assert_list_response_contains_exactly_by_id(
            all_payment_methods, [payment_method3, payment_method2, payment_method1]
        )
        self.assert_list_response_contains_exactly_by_id(
            payment_methods_after_last_id, [payment_method2, payment_method1]
        )
