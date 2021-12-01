import unittest

from mock import patch

from securionpay import disputes


@patch("securionpay.resource.Resource.request")
class TestCredits(unittest.TestCase):
    def test_get(self, request):
        disputes.get("disputeId")
        request.assert_called_once_with("GET", "/disputes/disputeId", None)

    def test_update(self, request):
        disputes.update("disputeId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/disputes/disputeId", {"some_param": "some_value"}
        )

    def test_close(self, request):
        disputes.close("disputeId")
        request.assert_called_once_with("POST", "/disputes/disputeId/close", None)

    def test_list(self, request):
        disputes.list({"some_param": "some_value"})
        request.assert_called_once_with(
            "GET", "/disputes", {"some_param": "some_value"}
        )
