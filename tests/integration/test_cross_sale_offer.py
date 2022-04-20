from .data.cross_sale_offers import valid_cross_sale_offer_with_charge

from .testcase import TestCase


class TestCrossSaleOffer(TestCase):
    def test_create_and_get(self, api):
        # given
        offer_req = valid_cross_sale_offer_with_charge()

        # when
        created = api.cross_sale_offers.create(offer_req)
        got = api.cross_sale_offers.get(created["id"])

        # then
        assert got["id"] is not None
        assert got["description"] == offer_req["description"]
        assert got["title"] == offer_req["title"]
        assert got["termsAndConditionsUrl"] == offer_req["termsAndConditionsUrl"]
        assert got["template"] == offer_req["template"]
        assert got["companyName"] == offer_req["companyName"]
        assert got["companyLocation"] == offer_req["companyLocation"]
        assert got["charge"]["amount"] == offer_req["charge"]["amount"]
        assert got["charge"]["currency"] == offer_req["charge"]["currency"]

    def test_update(self, api):
        # given
        offer_req = valid_cross_sale_offer_with_charge()
        created = api.cross_sale_offers.create(offer_req)

        # when
        updated = api.cross_sale_offers.update(
            created["id"], {"description": "updated description"}
        )

        # then
        assert created["description"] == offer_req["description"]
        assert updated["description"] == "updated description"
        assert updated["charge"]["amount"] == offer_req["charge"]["amount"]
        assert updated["charge"]["currency"] == offer_req["charge"]["currency"]

    def test_delete(self, api):
        # given
        offer_req = valid_cross_sale_offer_with_charge()
        created = api.cross_sale_offers.create(offer_req)

        # when
        api.cross_sale_offers.delete(created["id"])
        updated = api.cross_sale_offers.get(created["id"])

        # then
        assert "deleted" not in created
        assert updated["deleted"]

    def test_list(self, api):
        # given
        offer_req = valid_cross_sale_offer_with_charge()
        offer1 = api.cross_sale_offers.create(offer_req)
        offer2 = api.cross_sale_offers.create(offer_req)
        offer3 = api.cross_sale_offers.create(offer_req)

        # when
        all_offers = api.cross_sale_offers.list({"limit": 100})
        offers_after_last_id = api.cross_sale_offers.list(
            {"limit": 100, "startingAfterId": offer3["id"]}
        )

        # then
        self.assertListResponseContainsInAnyOrderById(
            all_offers, [offer3, offer2, offer1]
        )
        self.assertListResponseContainsInAnyOrderById(
            offers_after_last_id, [offer2, offer1]
        )
