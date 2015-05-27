import requests

from vegadns_client.store.file import AccessTokenStoreFile


class client(object):
    def __init__(key, secret, host, store=None):
        self.key = key
        self.secret = secret
        self.host = host
        if store is None:
            store = AccessTokenStoreFile(key, secret, host)
        self.store = store
        self.access_token = store.get_access_token()
        self.api_client = ApiClient(host, self.access_token)


class ApiClient(object):
    def __init__(self, host, access_token=None):
        self.host = host
        self.access_token = access_token

    def get(self, path):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.get(self.host + path, headers=headers)

    def post(self, path, data=None):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.post(self.host + path, headers=headers, data=data)

    def put(self, path, data=None):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.put(self.host + path, headers=headers, data=data)
