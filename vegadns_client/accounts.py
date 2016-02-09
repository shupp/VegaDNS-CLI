from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Accounts(AbstractResourceCollection):
    def __call__(self, search, filter=None):
        # filter will be supported later
        query_params = {}
        if search:
            query_params["search"] = search

        r = self.client.get("/accounts", params=query_params)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        accounts = []
        for account in decoded["accounts"]:
            a = Account(self.client)
            a.values = account
            accounts.append(a)

        return accounts

    def create(self, data):
        r = self.client.post(
            "/accounts",
            data=data
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = Account(self.client)
        m.values = decoded["account"]

        return m


class Account(AbstractResource):
    def __call__(self, account_id):
        r = self.client.get("/accounts/" + str(account_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["account"]

        return self

    def delete(self):
        if self.values.get('account_id', False) is False:
            raise ClientException(400, "account_id is not set")

        r = self.client.delete(
            "/accounts/" + str(self.values["account_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, data):
        if self.values.get('account_id', False) is False:
            raise ClientException(400, "account_id is not set")

        r = self.client.put(
            "/accounts/" + str(self.values["account_id"]),
            data=data
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["account"]

        return self
