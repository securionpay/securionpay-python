def valid_cross_sale_offer_with_charge():
    return {
        "charge": {
            "amount": 1000,
            "currency": "EUR",
        },
        "title": "Test Title",
        "description": "Test Description",
        "termsAndConditionsUrl": "https://github.com/securionpay",
        "template": "text_only",
        "companyName": "SecurionPay Tests",
        "companyLocation": "CH",
    }
