import unittest

import securionpay

class TestCase(unittest.TestCase):
    def setUp(self):
        self.gateway = securionpay.SecurionPayGateway('pr_test_tXHm9qV9qV9bjIRHcQr9PLPa')

    def tearDown(self):
        self.gateway = None
