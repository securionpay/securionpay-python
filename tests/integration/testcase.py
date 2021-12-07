import os
import unittest

from dotenv import load_dotenv

import securionpay as api

load_dotenv()


class TestCase(unittest.TestCase):
    def setUp(self):
        api.secret_key = os.getenv("SECRET_KEY")

    def tearDown(self):
        api.secret_key = None

    def assertSecurionPayException(self, fun, *args, **kwargs):
        try:
            fun(*args, **kwargs)
        except api.SecurionPayException as e:
            return e
        except Exception as e:
            self.fail("Wrong exception type received: %s" % str(type(e)))
        else:
            self.fail("Didn't receive exception")

    def assertCardMatchesRequest(self, card, card_req):
        self.assertEqual(card["first6"], card_req["number"][:6])
        self.assertEqual(card["last4"], card_req["number"][-4:])
        self.assertEqual(card["expMonth"], card_req["expMonth"])
        self.assertEqual(card["expYear"], card_req["expYear"])
        self.assertEqual(card["cardholderName"], card_req["cardholderName"])

    def assertListResponseContainsExactlyById(self, response, objects):
        response_ids = list(map(lambda o: o["id"], response["list"]))
        object_ids = list(map(lambda o: o["id"], objects))
        self.assertEqual(response_ids, object_ids)

    def assertListResponseContainsInAnyOrderById(self, response, objects):
        response_ids = list(map(lambda o: o["id"], response["list"]))
        object_ids = list(map(lambda o: o["id"], objects))
        for oid in object_ids:
            self.assertIn(oid, response_ids)
