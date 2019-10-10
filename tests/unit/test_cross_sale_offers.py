import unittest
from mock import patch
from securionpay import cross_sale_offers


@patch("securionpay.resource.Resource.request")
class TestCrossSaleOffers(unittest.TestCase):
    def test_create(self, request):
        cross_sale_offers.create({"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/cross_sale_offers", {"some_param": "some_value"}
        )

    def test_get(self, request):
        cross_sale_offers.get("crossSaleOfferId")
        request.assert_called_once_with(
            "GET", "/cross_sale_offers/crossSaleOfferId", None
        )

    def test_update(self, request):
        cross_sale_offers.update("crossSaleOfferId", {"some_param": "some_value"})
        request.assert_called_once_with(
            "POST", "/cross_sale_offers/crossSaleOfferId", {"some_param": "some_value"}
        )

    def test_delete(self, request):
        cross_sale_offers.delete("crossSaleOfferId")
        request.assert_called_once_with(
            "DELETE", "/cross_sale_offers/crossSaleOfferId", None
        )

    def test_list(self, request):
        cross_sale_offers.list({"some_param": "some_value"})
        request.assert_called_once_with(
            "GET", "/cross_sale_offers", {"some_param": "some_value"}
        )
