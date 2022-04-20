import sys

import requests

import securionpay as api
from securionpay.__version__ import __version__


class Resource(object):
    def name(self):
        return self.__class__.__name__.lower()

    def _get(self, path, params=None, url=None):
        return self.__request("GET", path, params=params, url=url)

    def _post(self, path, json=None, url=None):
        return self.__request("POST", path, json=json, url=url)

    def _multipart(self, path, params=None, files=None, url=None):
        return self.__request("POST", path, params=params, files=files, url=url)

    def _delete(self, path, params=None, url=None):
        return self.__request("DELETE", path, params=params, url=url)

    @classmethod
    def __request(cls, method, path, params=None, json=None, files=None, url=None):
        if url is None:
            url = api.api_url.rstrip("/")
        resp = requests.request(
            method,
            url=url + path,
            auth=(api.secret_key, ""),
            headers=cls.__create_headers(),
            files=files,
            params=params,
            json=json,
        )

        json = resp.json()
        if resp.status_code == 200:
            return json
        error = json.get("error")
        if error is None:
            raise api.SecurionPayException("Internal error", None, json, None, None)
        raise api.SecurionPayException(
            error.get("type"),
            error.get("code"),
            error.get("message"),
            error.get("charge_id"),
            error.get("blacklist_rule_id"),
        )

    @classmethod
    def __create_headers(cls):
        user_agent = "SecurionPay-Python/%s (Python/%s.%s.%s)" % (
            __version__,
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
        )

        return {"User-Agent": user_agent}
