from .data.cross_sale_offers import valid_cross_sale_offer_with_charge

from .testcase import api, TestCase


class TestCrossSaleOffer(TestCase):
    def test_create_and_get(self):
        # given
        offer_req = valid_cross_sale_offer_with_charge()

        # when
        created = api.cross_sale_offers.create(offer_req)
        got = api.cross_sale_offers.get(created["id"])

        # then
        self.assertIsNotNone(got["id"])
        self.assertEqual(got["description"], offer_req["description"])
        self.assertEqual(got["title"], offer_req["title"])
        self.assertEqual(
            got["termsAndConditionsUrl"], offer_req["termsAndConditionsUrl"]
        )
        self.assertEqual(got["template"], offer_req["template"])
        self.assertEqual(got["companyName"], offer_req["companyName"])
        self.assertEqual(got["companyLocation"], offer_req["companyLocation"])
        self.assertEqual(got["charge"]["amount"], offer_req["charge"]["amount"])
        self.assertEqual(got["charge"]["currency"], offer_req["charge"]["currency"])

    def test_update(self):
        # given
        offer_req = valid_cross_sale_offer_with_charge()
        created = api.cross_sale_offers.create(offer_req)

        # when
        updated = api.cross_sale_offers.update(
            created["id"], {"description": "updated description"}
        )

        # then
        self.assertEqual(created["description"], offer_req["description"])
        self.assertEqual(updated["description"], "updated description")
        self.assertEqual(updated["charge"]["amount"], offer_req["charge"]["amount"])
        self.assertEqual(updated["charge"]["currency"], offer_req["charge"]["currency"])

    def test_delete(self):
        # given
        offer_req = valid_cross_sale_offer_with_charge()
        created = api.cross_sale_offers.create(offer_req)

        # when
        api.cross_sale_offers.delete(created["id"])
        updated = api.cross_sale_offers.get(created["id"])

        # then
        self.assertNotIn("deleted", created)
        self.assertTrue(updated["deleted"])

    def test_list(self):
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
