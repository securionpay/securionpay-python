import testcase


class TestCards(testcase.TestCase):
    def test_create(self):
        customers = self.gateway.customers.list()
        card = self.gateway.cards.create(customers[0]['id'], {
            'number': '4242424242424242',
            'expMonth': '12',
            'expYear': '2020',
            'cvc': '123',
            'cardholderName': 'John Smith'
        })

    def test_list(self):
        customers = self.gateway.customers.list()
        cards = self.gateway.cards.list(customers[0]['id'])
        self.assertEquals(len(cards), 1)
