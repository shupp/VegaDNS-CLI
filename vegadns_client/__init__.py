import requests

from vegadns_client.store.file import AccessTokenStoreFile
from vegadns_client.groups import Groups, Group
from vegadns_client.domains import Domains, Domain
from vegadns_client.records import Records, Record
from vegadns_client.default_records import DefaultRecords, DefaultRecord
from vegadns_client.exports import Export
from vegadns_client.groupmembers import GroupMembers, GroupMember
from vegadns_client.domaingroupmaps import DomainGroupMaps, DomainGroupMap
from vegadns_client.accounts import Accounts, Account
from vegadns_client.updatedata import UpdateData
from vegadns_client.apikeys import ApiKeys, ApiKey


class client(object):
    def __init__(self, key, secret, host, store=None, version=1.0):
        self._key = key
        self._secret = secret
        self._host = host
        if store is None:
            store = AccessTokenStoreFile(key, secret, host)
        self._store = store
        self._access_token = store.get_access_token()
        self._api_client = ApiClient(host, self._access_token, version)

        # resources
        self.accounts = Accounts(self._api_client)
        self.account = Account(self._api_client)
        self.groups = Groups(self._api_client)
        self.group = Group(self._api_client)
        self.default_record = DefaultRecord(self._api_client)
        self.default_records = DefaultRecords(self._api_client)
        self.domains = Domains(self._api_client)
        self.domain = Domain(self._api_client)
        self.records = Records(self._api_client)
        self.record = Record(self._api_client)
        self.export = Export(self._api_client)
        self.groupmember = GroupMember(self._api_client)
        self.groupmembers = GroupMembers(self._api_client)
        self.domaingroupmap = DomainGroupMap(self._api_client)
        self.domaingroupmaps = DomainGroupMaps(self._api_client)
        self.updatedata = UpdateData(self._api_client)
        self.apikey = ApiKey(self._api_client)
        self.apikeys = ApiKeys(self._api_client)


class ApiClient(object):
    def __init__(self, host, access_token=None, version=1.0):
        self.host = host.rtrim("/") + "/" + str(version)
        self.access_token = access_token

    def get(self, path, params=None):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.get(self.host + path, headers=headers, params=params)

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
