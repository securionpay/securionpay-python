Python library for SecurionPay API
===================================

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
import securionpay

gateway = securionpay.SecurionPayGateway('pk_test_myprivatekey')

try:
    customer = gateway.customers.create({
        'email': 'user@example.com',
        'description': 'User description'
    })
    card = gateway.cards.create(customer['id'], {
        'number': '4242424242424242',
        'expMonth': '12',
        'expYear': '2020',
        'cvc': '123',
        'cardholderName': 'John Smith'
    })
except securionpay.SecurionPayException as e:
    print(e)
```

API reference
-------------

When ``params`` is one of method arguments please refer to detailed API docs (linked) for all available fields

- customers
    - [create(params)](https://securionpay.com/docs/api#customer-create)
    - [get(customerId)](https://securionpay.com/docs/api#customer-retrieve)
    - [list([params])](https://securionpay.com/docs/api#customer-list)
- cards
    - [create(customerId, params)](https://securionpay.com/docs/api#card-create)
    - [get(customerId, cardId)](https://securionpay.com/docs/api#card-retrieve)
    - [list(customerId, [params])](https://securionpay.com/docs/api#card-list)

Developing
----------

To run integration tests and check test coverage:
```
coverage run --source securionpay setup.py test
coverage report -m
```
