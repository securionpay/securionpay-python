Python library for SecurionPay API
===================================
[![Build Status](https://travis-ci.org/securionpay/securionpay-python.svg?branch=master)](https://travis-ci.org/securionpay/securionpay-python)
[![Code Climate](https://codeclimate.com/github/securionpay/securionpay-python/badges/gpa.svg)](https://codeclimate.com/github/securionpay/securionpay-python)

Installation
------------

```
pip install securionpay
```

Quick start
-----------

```
import securionpay as api
api.secret_key = 'pk_test_myprivatekey'

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
- subscriptions
    - [create(customerId, params)](https://securionpay.com/docs/api#subscription-create)
    - [get(customerId, subscriptionId)](https://securionpay.com/docs/api#subscription-retrieve)
    - [update(customerId, subscriptionId, params)](https://securionpay.com/docs/api#subscription-update)
    - [cancel(customerId, subscriptionId, [params])](https://securionpay.com/docs/api#subscription-cancel)
    - [list(customerId, [params])](https://securionpay.com/docs/api#subscription-list)
- plans
    - [create(params)](https://securionpay.com/docs/api#plan-create)
    - [get(planId)](https://securionpay.com/docs/api#plan-retrieve)
    - [update(planId, params)](https://securionpay.com/docs/api#plan-update)
    - [delete(planId)](https://securionpay.com/docs/api#plan-delete)
    - [list([params])](https://securionpay.com/docs/api#plan-list)
- events
    - [get(eventId)](https://securionpay.com/docs/api#event-retrieve)
    - [list([params])](https://securionpay.com/docs/api#event-list)
- tokens
    - [create(params)](https://securionpay.com/docs/api#token-create)
    - [get(tokenId)](https://securionpay.com/docs/api#token-retrieve)
- blacklist
    - [create(params)](https://securionpay.com/docs/api#blacklist-rule-create)
    - [get(blacklistRuleId)](https://securionpay.com/docs/api#blacklist-rule-retrieve)
    - [delete(blacklistRuleId)](https://securionpay.com/docs/api#blacklist-rule-delete)
    - [list([params])](https://securionpay.com/docs/api#blacklist-rule-list)
- checkoutRequest
    - [sign(checkoutRequestDictOrJson)](https://securionpay.com/docs/api#checkout-request-sign)
- crossSaleOffers
    - [create(params)](https://securionpay.com/docs/api#cross-sale-offer-create)
    - [get(crossSaleOfferId)](https://securionpay.com/docs/api#cross-sale-offer-retrieve)
    - [update(crossSaleOfferId, params)](https://securionpay.com/docs/api#cross-sale-offer-update)
    - [delete(crossSaleOfferId)](https://securionpay.com/docs/api#cross-sale-offer-delete)
    - [list([params])](https://securionpay.com/docs/api#cross-sale-offer-list)
- customerRecords
    - [buy(params)](https://securionpay.com/docs/api#customer-record-create)
    - [refresh(customerRecordId, [params])](https://securionpay.com/docs/api#customer-record-refresh)
    - [get(customerRecordId)](https://securionpay.com/docs/api#customer-record-retrieve)
    - [list([params])](https://securionpay.com/docs/api#customer-record-list)
    - [getFee(customerRecordId, customerRecordFeeId)](https://securionpay.com/docs/api#customer-record-fee-retrieve)
    - [listFees(customerRecordId, [params])](https://securionpay.com/docs/api#customer-record-fee-list)
    - [getProfit(customerRecordId, customerRecordProfitId)](https://securionpay.com/docs/api#customer-record-profit-retrieve)
    - [listProfits(customerRecordId, [params])](https://securionpay.com/docs/api#customer-record-profit-list)

Developing
----------

Optionally setup a virtual environment (requires the `virtualenv` python package):
```sh
virtualenv env
source env/bin/activate
```

Install the package dependencies:
```sh
pip install -r requirements.txt
pip install -r test_requirements.txt
```

To connect to different backend:
```
import securionpay as api
api.secret_key = 'pk_test_myprivatekey'
api.url = 'http://mysecurionenv.com'
```

To run unit tests and check test coverage:
```
nosetests -w tests/unit --with-coverage --cover-package=securionpay
coverage report -m
```

To run integration tests:
```
SECRET_KEY=pk_test_myprivatekey nosetests -w tests/integration
```

Format the package files using `black`:
```sh
black setup.py securionpay/ tests/
```

Documentation
----------

For further information, please refer to our official documentation at https://securionpay.com/docs.
