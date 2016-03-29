Python library for SecurionPay API
===================================
[![Build Status](https://travis-ci.org/securionpay/securionpay-python.svg?branch=master)](https://travis-ci.org/securionpay/securionpay-python)
[![Code Climate](https://codeclimate.com/github/securionpay/securionpay-python/badges/gpa.svg)](https://codeclimate.com/github/securionpay/securionpay-python)

For detailed description of parameters for available methods
please visit https://securionpay.com/docs/api

Installation
------------

```
pip install securionpay
```

Quick start
-----------

```
import securionpay as api
api.private_key = 'pk_test_myprivatekey'

try:
    customer = api.customers.create({
        'email': 'user@example.com',
        'description': 'User description'
    })
    card = api.cards.create(customer['id'], {
        'number': '4242424242424242',
        'expMonth': '12',
        'expYear': '2020',
        'cvc': '123',
        'cardholderName': 'John Smith'
    })
    charge = api.charges.create({
        'amount': 1000,
        'currency': 'EUR',
        'customerId': card['customerId']
    })
except securionpay.SecurionPayException as e:
    print(e)
```

API reference
-------------

When ``params`` is one of method arguments please refer to detailed API docs (linked) for all available fields

- charges
    - [create(params)](https://securionpay.com/docs/api#charge-create)
    - [get(chargeId)](https://securionpay.com/docs/api#charge-retrieve)
    - [update(chargeId, params)](https://securionpay.com/docs/api#charge-update)
    - [capture(chargeId)](https://securionpay.com/docs/api#charge-capture)
    - [refund(chargeId, [params])](https://securionpay.com/docs/api#charge-capture)
    - [list([params])](https://securionpay.com/docs/api#charge-list)
- customers
    - [create(params)](https://securionpay.com/docs/api#customer-create)
    - [get(customerId)](https://securionpay.com/docs/api#customer-retrieve)
    - [update(customerId, params)](https://securionpay.com/docs/api#customer-update)
    - [delete(customerId)](https://securionpay.com/docs/api#customer-delete)
    - [list([params])](https://securionpay.com/docs/api#customer-list)
- cards
    - [create(customerId, params)](https://securionpay.com/docs/api#card-create)
    - [get(customerId, cardId)](https://securionpay.com/docs/api#card-retrieve)
    - [update(customerId, cardId, params)](https://securionpay.com/docs/api#card-update)
    - [delete(customerId, cardId)](https://securionpay.com/docs/api#card-delete)
    - [list(customerId, [params])](https://securionpay.com/docs/api#card-list)

Developing
----------

To connect to different backend:
```
import securionpay as api
api.private_key = 'pk_test_myprivatekey'
api.url = 'http://mysecurionenv.com'
```

To run unit tests and check test coverage:
```
nosetests -w tests/unit --with-coverage --cover-package=securionpay
coverage report -m
```

To run integration tests:
```
PRIVATE_KEY=pk_test_myprivatekey nosetests -w tests/integration
```

To run integration tests against environment other than default:
```
PRIVATE_KEY=pk_test_myprivatekey URL=http://mysecurionenv.com nosetests -w tests/integration
```
