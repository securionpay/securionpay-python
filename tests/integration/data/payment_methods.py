def payment_method(customerId=None):
    req = {"type": "alipay", "billing": {"name": "Jack Sparrow"}}
    if customerId is not None:
        req["customerId"] = customerId
    return req
