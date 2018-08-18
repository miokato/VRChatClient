import requests
from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth
from django.conf import settings


def parse_params(params):
    if not isinstance(params, dict):
        raise TypeError('params is dict')
    queries = '?'
    for i, (k, v) in enumerate(params.items()):
        queries += '{k}={v}'.format(k=k, v=v)
        if not (i == len(params.items()) - 1):
            queries += '&'
    return queries


class VRChatClient:
    base_path = settings.VRC_BASE_URL

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api_key = self._get_apikey()
        self.auth_token = self._get_auth_token()

    def search_users(self, keyword=None, n=10):
        if keyword is None:
            return self.get('users', n=n)
        return self.get('users', search=keyword, n=n)

    def get(self, path, **params):
        queries = parse_params(params)
        path += queries
        url = urljoin(self.base_path, path)
        r = requests.get(
            url,
            params={
                'apiKey': self.api_key,
                'authToken': self.auth_token,
            })
        return r.json()

    def _get_apikey(self):
        url = '{}/config'.format(self.base_path)
        r = requests.get(url)
        return r.json()['clientApiKey']

    def _get_auth_token(self):
        url = '{}/auth/user'.format(self.base_path)
        r = requests.get(
            url,
            params={'apiKey': self.api_key},
            auth=HTTPBasicAuth(self.username, self.password))
        return r.cookies['auth']
