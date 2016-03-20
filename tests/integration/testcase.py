import os
import unittest
import securionpay as api


class TestCase(unittest.TestCase):
    def setUp(self):
        api.private_key = os.getenv('PRIVATE_KEY', 'pr_test_FjW0q2HMs40Jj3KGua5294sp')
        api.url = os.getenv('URL', 'https://api.securionpay.com')

    def tearDown(self):
        api.private_key = None
