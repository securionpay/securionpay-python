import securionpay as api
import requests


class Resource(object):
    def name(self):
        return self.__class__.__name__.lower()

    @staticmethod
    def request(method, parts, params=None):
        url = '/'.join([str(part) for part in [api.url.rstrip('/')] + parts])
        resp = requests.request(method, url, json=params, auth=(api.private_key, ''))
        json = resp.json()
        if resp.status_code == 200:
            return json
        error = json.get('error')
        if error is None:
            raise api.SecurionPayException('Internal error', None, json, None, None)
        raise api.SecurionPayException(error.get('type'), error.get('code'), error.get('message'),
                                       error.get('charge_id'), error.get('blacklist_rule_id'))
