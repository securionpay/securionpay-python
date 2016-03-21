import requests
import securionpay as api


def create_url(parts):
    return "/".join([str(part) for part in parts])


def request(method, path, params=None):
    resp = requests.request(method, '/'.join([api.url.rstrip('/'), path]), json=params, auth=(api.private_key, ''))
    json = resp.json()
    if resp.status_code == 200:
        return json
    error = json.get('error')
    if error is None:
        raise api.SecurionPayException('Internal error', None, json, None, None)
    raise api.SecurionPayException(error.get('type'), error.get('code'), error.get('message'),
                                   error.get('charge_id'), error.get('blacklist_rule_id'))
