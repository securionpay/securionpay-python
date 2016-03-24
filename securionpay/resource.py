import securionpay as api
import requests


class Resource(object):
    def name(self):
        return self.__class__.__name__.lower()

    def _get(self, path, params=None):
        return self.request('GET', path, params)

    def _post(self, path, params=None):
        return self.request('POST', path, params)

    def _delete(self, path, params=None):
        return self.request('DELETE', path, params)

    @staticmethod
    def request(method, path, params=None):
        url = api.url.rstrip('/') + '/' + path
        resp = requests.request(method, url, json=params, auth=(api.private_key, ''))
        json = resp.json()
        if resp.status_code == 200:
            return json
        error = json.get('error')
        if error is None:
            raise api.SecurionPayException('Internal error', None, json, None, None)
        raise api.SecurionPayException(error.get('type'), error.get('code'), error.get('message'),
                                       error.get('charge_id'), error.get('blacklist_rule_id'))
