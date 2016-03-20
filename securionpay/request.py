import requests
from securionpay import (SecurionPayException, private_key, url)


def request(method, path, params=None):
    resp = requests.request(method, '/'.join([url.rstrip('/'), path]), json=params, auth=(private_key, ''))
    if resp.status_code == 200:
        return resp.json()
    raise SecurionPayException('Server response status code: %d (%s)\nRequest parts: %s\nParams: %s' %
                               (resp.status_code, resp.reason, path, str(params)))
