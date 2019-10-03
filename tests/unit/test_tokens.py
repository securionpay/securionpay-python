import unittest
from mock import patch
from securionpay import tokens


@patch("securionpay.resource.Resource.request")
class TestTokens(unittest.TestCase):
    def test_create(self, request):
        tokens.create({"some_param": "some_value"})
        request.assert_called_once_with("POST", "/tokens", {"some_param": "some_value"})

    def test_get(self, request):
        tokens.get("cusId")
        request.assert_called_once_with("GET", "/tokens/cusId", None)
