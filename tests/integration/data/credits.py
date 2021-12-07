from tests.integration.data.cards import valid_card_req


def valid_credit_req(card=valid_card_req(), customerId=None):
    req = {
        "amount": 1000,
        "currency": "EUR",
        "description": "Test Description",
        "metadata": {"key": "test value"},
    }
    if customerId is not None:
        req["customerId"] = customerId
    if card is not None:
        req["card"] = card
    return req
