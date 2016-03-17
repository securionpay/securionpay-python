api_url = 'https://api.securionpay.com'
api_key = 'pr_test_tXHm9qV9qV9bjIRHcQr9PLPa'

from securionpay.exception import SecurionPayException
from securionpay import resources

cards = resources.Cards()
customers = resources.Customers()
charges = resources.Charges()
