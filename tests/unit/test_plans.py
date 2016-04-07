import unittest
from mock import patch
from securionpay import plans


@patch('securionpay.resource.Resource.request')
class TestPlans(unittest.TestCase):
    def test_create(self, request):
        plans.create({'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        '/plans',
                                        {'some_param': 'some_value'})

    def test_get(self, request):
        plans.get("cusId")
        request.assert_called_once_with('GET',
                                        '/plans/cusId',
                                        None)

    def test_update(self, request):
        plans.update("cusId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        '/plans/cusId',
                                        {'some_param': 'some_value'})

    def test_delete(self, request):
        plans.delete("cusId")
        request.assert_called_once_with('DELETE',
                                        '/plans/cusId',
                                        None)

    def test_list(self, request):
        plans.list({'some_param': 'some_value'})
        request.assert_called_once_with('GET',
                                        '/plans',
                                        {'some_param': 'some_value'})
