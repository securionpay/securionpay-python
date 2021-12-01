import os
import unittest
import securionpay as api


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
