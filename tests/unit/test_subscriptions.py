import unittest
from mock import patch
from securionpay import subscriptions


@patch('securionpay.resource.Resource.request')
class TestSubscriptions(unittest.TestCase):
    def test_create(self, request):
        subscriptions.create("cusId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        '/customers/cusId/subscriptions',
                                        {'some_param': 'some_value'})

    def test_get(self, request):
        subscriptions.get("cusId", "subscriptionId")
        request.assert_called_once_with('GET',
                                        '/customers/cusId/subscriptions/subscriptionId',
                                        None)

    def test_update(self, request):
        subscriptions.update("cusId", "subscriptionId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        '/customers/cusId/subscriptions/subscriptionId',
                                        {'some_param': 'some_value'})

    def test_cancel(self, request):
        subscriptions.cancel("cusId", "subscriptionId")
        request.assert_called_once_with('DELETE',
                                        '/customers/cusId/subscriptions/subscriptionId',
                                        None)

    def test_list(self, request):
        subscriptions.list("cusId", {'some_param': 'some_value'})
        request.assert_called_once_with('GET',
                                        '/customers/cusId/subscriptions',
                                        {'some_param': 'some_value'})
