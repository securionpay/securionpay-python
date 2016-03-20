import unittest

from mock import (patch, MagicMock)

from securionpay import charges


@patch('securionpay.resources.request')
class TestCharges(unittest.TestCase):
    def test_create(self, request):
        charges.create({'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        'charges',
                                        {'some_param': 'some_value'})

    def test_get(self, request):
        charges.get("chargeId")
        request.assert_called_once_with('GET',
                                        'charges/chargeId',
                                        None)

    def test_update(self, request):
        charges.update("chargeId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        'charges/chargeId',
                                        {'some_param': 'some_value'})

    def test_capture(self, request):
        charges.capture("chargeId")
        request.assert_called_once_with('POST',
                                        'charges/chargeId/capture',
                                        None)

    def test_refund(self, request):
        charges.refund("chargeId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        'charges/chargeId/refund',
                                        {'some_param': 'some_value'})

    def test_list(self, request):
        request.return_value = MagicMock(spec=['__getitem__'])
        charges.list({'some_param': 'some_value'})
        request.assert_called_once_with('GET',
                                        'charges',
                                        {'some_param': 'some_value'})
        request.return_value.__getitem__.assert_called_once_with('list')
