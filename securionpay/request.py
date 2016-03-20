import requests
from securionpay import (SecurionPayException, api_key, api_url)


def request(method, path, params=None):
    resp = requests.request(method, '/'.join([api_url.rstrip('/'), path]), json=params, auth=(api_key, ''))
    if resp.status_code == 200:
        return resp.json()
    raise SecurionPayException('Server response status code: %d (%s)\nRequest parts: %s\nParams: %s' %
                               (resp.status_code, resp.reason, path, str(params)))
