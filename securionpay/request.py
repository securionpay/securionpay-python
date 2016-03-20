import requests
import securionpay as api


def request(method, path, params=None):
    resp = requests.request(method, '/'.join([api.url.rstrip('/'), path]), json=params, auth=(api.private_key, ''))
    if resp.status_code == 200:
        return resp.json()
    raise api.SecurionPayException('Server response status code: %d (%s)\nRequest parts: %s\nParams: %s' %
                               (resp.status_code, resp.reason, path, str(params)))
