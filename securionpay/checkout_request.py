import base64
import hashlib
import hmac
import json

import securionpay as api


def sign(checkout_request):
    if not isinstance(checkout_request, str):
        checkout_request = json.dumps(
            checkout_request, sort_keys=True, separators=(",", ":")
        )

    digest = hmac.new(
        api.secret_key.encode(),
        msg=checkout_request.encode(),
        digestmod=hashlib.sha256,
    ).hexdigest()
    return base64.b64encode((digest + "|" + checkout_request).encode()).decode()
