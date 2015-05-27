import requests

from vegadns_client.store.file import AccessTokenStoreFile
from vegadns_client.groups import Groups, Group
from vegadns_client.domains import Domains, Domain
from vegadns_client.records import Records, Record


class client(object):
    def __init__(self, key, secret, host, store=None):
        self._key = key
        self._secret = secret
        self._host = host
        if store is None:
            store = AccessTokenStoreFile(key, secret, host)
        self._store = store
        self._access_token = store.get_access_token()
        self._api_client = ApiClient(host, self._access_token)

        # resources
        self.groups = Groups(self._api_client)
        self.group = Group(self._api_client)
        self.domains = Domains(self._api_client)
        self.domain = Domain(self._api_client)
        self.records = Records(self._api_client)
        self.record = Record(self._api_client)


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

    def delete(self, path):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.delete(self.host + path, headers=headers)

    def patch(self, path, data=None):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.patch(self.host + path, headers=headers, data=data)
