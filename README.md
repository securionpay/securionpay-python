Python library for SecurionPay API
===================================
[![Build](https://github.com/securionpay/securionpay-python/actions/workflows/build.yml/badge.svg)](https://github.com/securionpay/securionpay-python/actions/workflows/build.yml)

Installation
------------

```
pip install securionpay
```

Quick start
-----------

```python
import securionpay as securionpay

securionpay.secret_key = 'pk_test_my_secret_key'

try:
    customer = securionpay.customers.create({
        'email': 'user@example.com',
        'description': 'User description'
    })
    print("Created customer:", customer)
    card = securionpay.cards.create(customer['id'], {
        'number': '4242424242424242',
        'expMonth': '12',
        'expYear': '2023',
        'cvc': '123',
        'cardholderName': 'John Smith'
    })
    print("Created card:", card)
    charge = securionpay.charges.create({
      'amount': 1000,
      'currency': 'EUR',
      'customerId': card['customerId']
    })
    print("Created charge:", charge)
except securionpay.SecurionPayException as e:
  print(e)
```

API reference
-------------

Please refer to detailed API docs (linked) for all available fields

- charges
  - [create(params)](https://securionpay.com/docs/api#charge-create)
  - [get(charge_id)](https://securionpay.com/docs/api#charge-retrieve)
  - [update(charge_id, params)](https://securionpay.com/docs/api#charge-update)
  - [capture(charge_id)](https://securionpay.com/docs/api#charge-capture)
  - [refund(charge_id, [params])](https://securionpay.com/docs/api#charge-capture)
  - [list([params])](https://securionpay.com/docs/api#charge-list)
- customers
  - [create(params)](https://securionpay.com/docs/api#customer-create)
  - [get(customer_id)](https://securionpay.com/docs/api#customer-retrieve)
  - [update(customer_id, params)](https://securionpay.com/docs/api#customer-update)
  - [delete(customer_id)](https://securionpay.com/docs/api#customer-delete)
  - [list([params])](https://securionpay.com/docs/api#customer-list)
- cards
  - [create(customer_id, params)](https://securionpay.com/docs/api#card-create)
  - [get(customer_id, card_id)](https://securionpay.com/docs/api#card-retrieve)
  - [update(customer_id, card_id, params)](https://securionpay.com/docs/api#card-update)
  - [delete(customer_id, card_id)](https://securionpay.com/docs/api#card-delete)
  - [list(customer_id, [params])](https://securionpay.com/docs/api#card-list)
- subscriptions
  - [create(params)](https://securionpay.com/docs/api#subscription-create)
  - [get(subscription_id)](https://securionpay.com/docs/api#subscription-retrieve)
  - [update(subscription_id, params)](https://securionpay.com/docs/api#subscription-update)
  - [cancel(subscription_id, [params])](https://securionpay.com/docs/api#subscription-cancel)
  - [list([params])](https://securionpay.com/docs/api#subscription-list)
- plans
  - [create(params)](https://securionpay.com/docs/api#plan-create)
  - [get(plan_id)](https://securionpay.com/docs/api#plan-retrieve)
  - [update(plan_id, params)](https://securionpay.com/docs/api#plan-update)
  - [delete(plan_id)](https://securionpay.com/docs/api#plan-delete)
  - [list([params])](https://securionpay.com/docs/api#plan-list)
- events
  - [get(event_id)](https://securionpay.com/docs/api#event-retrieve)
  - [list([params])](https://securionpay.com/docs/api#event-list)
- tokens
  - [create(params)](https://securionpay.com/docs/api#token-create)
  - [get(token_id)](https://securionpay.com/docs/api#token-retrieve)
- blacklist
  - [create(params)](https://securionpay.com/docs/api#blacklist-rule-create)
  - [get(blacklist_rule_id)](https://securionpay.com/docs/api#blacklist-rule-retrieve)
  - [delete(blacklist_rule_id)](https://securionpay.com/docs/api#blacklist-rule-delete)
  - [list([params])](https://securionpay.com/docs/api#blacklist-rule-list)
- checkoutRequest
  - [sign(checkoutRequestObjectOrJson)](https://securionpay.com/docs/api#checkout-request-sign)
- crossSaleOffers
  - [create(params)](https://securionpay.com/docs/api#cross-sale-offer-create)
  - [get(cross_sale_offer_id)](https://securionpay.com/docs/api#cross-sale-offer-retrieve)
  - [update(cross_sale_offer_id, params)](https://securionpay.com/docs/api#cross-sale-offer-update)
  - [delete(cross_sale_offer_id)](https://securionpay.com/docs/api#cross-sale-offer-delete)
  - [list([params])](https://securionpay.com/docs/api#cross-sale-offer-list)
- credits
  - [create(params)](https://securionpay.com/docs/api#credit-create)
  - [get(credit_id)](https://securionpay.com/docs/api#credit-retrieve)
  - [update(credit_id, params)](https://securionpay.com/docs/api#credit-update)
  - [list([params])](https://securionpay.com/docs/api#credit-list)
- disputes
  - [get(dispute_id)](https://securionpay.com/docs/api#dispute-retrieve)
  - [update(dispute_id, params)](https://securionpay.com/docs/api#dispute-update)
  - [close(dispute_id)](https://securionpay.com/docs/api#dispute-close)
  - [list([params])](https://securionpay.com/docs/api#dispute-list)
- fileUploads
  - [upload(content, params)](https://securionpay.com/docs/api#file-upload-create)
  - [get(file_upload_id)](https://securionpay.com/docs/api#file-upload-retrieve)
  - [list([params])](https://securionpay.com/docs/api#file-upload-list)
- fraudWarnings
  - [get(fraud_warning_id)](https://securionpay.com/docs/api#fraud-warning-retrieve)
  - [list([params])](https://securionpay.com/docs/api#fraud-warning-list)

For further information, please refer to our official documentation
at [https://securionpay.com/docs](https://securionpay.com/docs).


Developing
----------

Optionally setup a virtual environment
```sh
python -m venv ./venv --clear
source ./venv/bin/activate 
```

Install the package dependencies:
```sh
pip install -r requirements.txt -r test_requirements.txt
```

To connect to different backend:

```python
import securionpay as api

api.secret_key = 'pk_test_my_secret_key'
api.api_url = 'https://api.mysecurionenv.com'
api.uploads_url = 'https://uploads.mysecurionenv.com'
```

To run tests:

```sh
SECRET_KEY=pk_test_my_secret_key pytest tests
```

Format the package files using `black`:

```sh
black setup.py securionpay/ tests/
```
