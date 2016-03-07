from securionpay import (Cards, Customers)


class SecurionPayGateway(object):
    def __init__(self, privateKey):
        self.privateKey = privateKey
        self.cards = Cards((privateKey, ""))
        self.customers = Customers((privateKey, ""))
