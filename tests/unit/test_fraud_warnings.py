import unittest

from mock import patch

from securionpay import fraud_warnings


@patch("securionpay.resource.Resource.request")
class TestFraudWarnings(unittest.TestCase):
    def test_get(self, request):
        fraud_warnings.get("fraudWarningId")
        request.assert_called_once_with("GET", "/fraud-warnings/fraudWarningId", None)

    def test_list(self, request):
        fraud_warnings.list({"some_param": "some_value"})
        request.assert_called_once_with(
            "GET", "/fraud-warnings", {"some_param": "some_value"}
        )
