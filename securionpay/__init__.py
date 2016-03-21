from securionpay.config import (private_key, url)
from securionpay.exception import SecurionPayException
from securionpay import resources
from securionpay import customer_resources

customers = resources.Customers()
charges = resources.Charges()
cards = customer_resources.Cards()
