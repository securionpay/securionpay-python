import unittest
from mock import patch
from securionpay import customer_records


@patch("securionpay.resource.Resource.request")
class TestCustomerRecords(unittest.TestCase):
    def test_buy(self, request):
        customer_records.buy({"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/customer-records", {"some_param": "some_value"}
        )

    def test_refresh(self, request):
        customer_records.refresh("customerRecordId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/customer-records/customerRecordId", {"some_param": "some_value"}
        )

    def test_get(self, request):
        customer_records.get("customerRecordId")
        request.assert_called_once_with(
            "GET", "/customer-records/customerRecordId", None
        )

    def test_list(self, request):
        customer_records.list({"some_param": "some_value"})
        request.assert_called_once_with(
            "GET", "/customer-records", {"some_param": "some_value"}
        )

    def test_get_fee(self, request):
        customer_records.get_fee("customerRecordId", "feeId")
        request.assert_called_once_with(
            "GET", "/customer-records/customerRecordId/fees/feeId", None
        )

    def test_list_fees(self, request):
        customer_records.list_fees("customerRecordId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "GET",
            "/customer-records/customerRecordId/fees",
            {"some_param": "some_value"},
        )

    def test_get_profit(self, request):
        customer_records.get_profit("customerRecordId", "profitId")
        request.assert_called_once_with(
            "GET", "/customer-records/customerRecordId/profits/profitId", None
        )

    def test_list_profits(self, request):
        customer_records.list_profits("customerRecordId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "GET",
            "/customer-records/customerRecordId/profits",
            {"some_param": "some_value"},
        )
