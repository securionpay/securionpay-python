from tests.integration import random_email


def valid_customer_req(email=random_email(), card=None):
    req = {"email": email}
    if card is not None:
        req["card"] = card
    return req
