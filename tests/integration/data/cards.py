def valid_card_req():
    return {
        "number": "4242424242424242",
        "expMonth": "12",
        "expYear": "2055",
        "cvc": "123",
        "cardholderName": "Python Test",
    }


def disputed_card_req():
    return {
        "number": "4242000000000018",
        "expMonth": "12",
        "expYear": "2055",
        "cvc": "123",
        "cardholderName": "Python Test",
    }


def fraud_warning_card_req():
    return {
        "number": "4242000000000208",
        "expMonth": "12",
        "expYear": "2055",
        "cvc": "123",
        "cardholderName": "Python Test",
    }
