import unittest
from mock import patch
from securionpay import blacklist


@patch("securionpay.resource.Resource.request")
class TestBlacklist(unittest.TestCase):
    def test_create(self, request):
        blacklist.create({"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/blacklist", {"some_param": "some_value"}
        )

    def test_get(self, request):
        blacklist.get("blackId")
        request.assert_called_once_with("GET", "/blacklist/blackId", None)

    def test_delete(self, request):
        blacklist.delete("blackId")
        request.assert_called_once_with("DELETE", "/blacklist/blackId", None)

    def test_list(self, request):
        blacklist.list({"some_param": "some_value"})
        request.assert_called_once_with(
            "GET", "/blacklist", {"some_param": "some_value"}
        )
