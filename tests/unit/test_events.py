import unittest
from mock import patch
from securionpay import events


@patch('securionpay.resource.Resource.request')
class TestEvents(unittest.TestCase):
    def test_get(self, request):
        events.get("eventId")
        request.assert_called_once_with('GET',
                                        '/events/eventId',
                                        None)

    def test_list(self, request):
        events.list({'some_param': 'some_value'})
        request.assert_called_once_with('GET',
                                        '/events',
                                        {'some_param': 'some_value'})
