import unittest
import securionpay as api
import json


class TestCheckoutRequest(unittest.TestCase):
    def setUp(self):
        api.private_key = "pr_test_bu0GRzw3MzhT10fpxa1j9OHJ"

    def test_from_string(self):
        self.assertEqual(
            api.checkout_request.sign('{"charge":{"amount":499,"currency":"EUR"}}'),
            "NTk1MjY3MmZjMjdjMjdkZjEyNDlhYjA3YTQ4NDE2NDdhYzcwOGM1MzdjYWQ3MDhjNDRlZWVkMDIzOWI0OTc0Ynx7ImNoYXJnZSI6eyJhbW91bnQiOjQ5OSwiY3VycmVuY3kiOiJFVVIifX0=",
        )

    def test_from_dict(self):
        self.assertEqual(
            api.checkout_request.sign(
                json.loads('{"charge":{"amount":499,"currency":"EUR"}}')
            ),
            "NTk1MjY3MmZjMjdjMjdkZjEyNDlhYjA3YTQ4NDE2NDdhYzcwOGM1MzdjYWQ3MDhjNDRlZWVkMDIzOWI0OTc0Ynx7ImNoYXJnZSI6eyJhbW91bnQiOjQ5OSwiY3VycmVuY3kiOiJFVVIifX0=",
        )
