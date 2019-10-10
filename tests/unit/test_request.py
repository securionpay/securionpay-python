import unittest
from mock import patch
import securionpay as api


@patch("securionpay.resource.requests")
class TestRequest(unittest.TestCase):
    def test_get(self, requests):
        requests.request.return_value.status_code = 200
        requests.request.return_value.json = lambda: ""
        api.resource.Resource.request("GET", "/some_url", {"some_param": "some_value"})
        requests.request.assert_called_once_with(
            "GET",
            api.url + "/some_url",
            auth=(api.private_key, ""),
            params={"some_param": "some_value"},
        )

    def test_post(self, requests):
        requests.request.return_value.status_code = 200
        requests.request.return_value.json = lambda: ""
        api.resource.Resource.request("POST", "/some_url", {"some_param": "some_value"})
        requests.request.assert_called_once_with(
            "POST",
            api.url + "/some_url",
            auth=(api.private_key, ""),
            json={"some_param": "some_value"},
        )

    def test_delete(self, requests):
        requests.request.return_value.status_code = 200
        requests.request.return_value.json = lambda: ""
        api.resource.Resource.request(
            "DELETE", "/some_url", {"some_param": "some_value"}
        )
        requests.request.assert_called_once_with(
            "DELETE",
            api.url + "/some_url",
            auth=(api.private_key, ""),
            params={"some_param": "some_value"},
        )
