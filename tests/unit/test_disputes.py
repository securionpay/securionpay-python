import unittest

from mock import patch

from securionpay import credits


@patch("securionpay.resource.Resource.request")
class TestDisputes(unittest.TestCase):
    def test_create(self, request):
        credits.create({"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/credits", {"some_param": "some_value"}
        )

    def test_get(self, request):
        credits.get("creditId")
        request.assert_called_once_with("GET", "/credits/creditId", None)

    def test_update(self, request):
        credits.update("creditId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/credits/creditId", {"some_param": "some_value"}
        )

    def test_list(self, request):
        credits.list({"some_param": "some_value"})
        request.assert_called_once_with("GET", "/credits", {"some_param": "some_value"})
