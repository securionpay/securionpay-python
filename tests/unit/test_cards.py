import unittest

from mock import (patch, MagicMock)

from securionpay import cards


@patch('securionpay.resources.request')
class TestCards(unittest.TestCase):
    def test_create(self, request):
        cards.create("cusId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        'customers/cusId/cards',
                                        {'some_param': 'some_value'})

    def test_get(self, request):
        cards.get("cusId", "cardId")
        request.assert_called_once_with('GET',
                                        'customers/cusId/cards/cardId',
                                        None)

    def test_update(self, request):
        cards.update("cusId", "cardId", {'some_param': 'some_value'})
        request.assert_called_once_with('POST',
                                        'customers/cusId/cards/cardId',
                                        {'some_param': 'some_value'})

    def test_delete(self, request):
        cards.delete("cusId", "cardId")
        request.assert_called_once_with('DELETE',
                                        'customers/cusId/cards/cardId',
                                        None)

    def test_list(self, request):
        request.return_value = MagicMock(spec=['__getitem__'])
        cards.list("cusId", {'some_param': 'some_value'})
        request.assert_called_once_with('GET',
                                        'customers/cusId/cards',
                                        {'some_param': 'some_value'})
        request.return_value.__getitem__.assert_called_once_with('list')
