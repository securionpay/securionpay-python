import unittest

from mock import (patch, MagicMock)

from securionpay import customers


@patch('securionpay.resource.Resource.request')
class TestCustomers(unittest.TestCase):
    def test_create(self, request):
        customers.create({'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        '/customers',
                                        {'some_param': 'some_value'})

    def test_get(self, request):
        customers.get("cusId")
        request.assert_called_once_with('GET',
                                        '/customers/cusId',
                                        None)

    def test_update(self, request):
        customers.update("cusId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        '/customers/cusId',
                                        {'some_param': 'some_value'})

    def test_delete(self, request):
        customers.delete("cusId")
        request.assert_called_once_with('DELETE',
                                        '/customers/cusId',
                                        None)

    def test_list(self, request):
        request.return_value = MagicMock(spec=['__getitem__'])
        customers.list({'some_param': 'some_value'})
        request.assert_called_once_with('GET',
                                        '/customers',
                                        {'some_param': 'some_value'})
        request.return_value.__getitem__.assert_called_once_with('list')
