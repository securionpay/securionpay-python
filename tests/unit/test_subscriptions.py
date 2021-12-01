import unittest

from mock import patch

from securionpay import subscriptions


@patch("securionpay.resource.Resource.request")
class TestSubscriptions(unittest.TestCase):
    def test_create(self, request):
        subscriptions.create({"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/subscriptions", {"some_param": "some_value"}
        )

    def test_get(self, request):
        subscriptions.get("subscriptionId")
        request.assert_called_once_with("GET", "/subscriptions/subscriptionId", None)

    def test_update(self, request):
        subscriptions.update("subscriptionId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "POST",
            "/subscriptions/subscriptionId",
            {"some_param": "some_value"},
        )

    def test_cancel(self, request):
        subscriptions.cancel("subscriptionId")
        request.assert_called_once_with("DELETE", "/subscriptions/subscriptionId", None)

    def test_list(self, request):
        subscriptions.list({"some_param": "some_value"})
        request.assert_called_once_with(
            "GET", "/subscriptions", {"some_param": "some_value"}
        )
