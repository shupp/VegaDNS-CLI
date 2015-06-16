from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Accounts(AbstractResourceCollection):
    def __call__(self, filter=None):
        # filter will be supported later
        r = self.client.get("/accounts")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        accounts = []
        for account in decoded["accounts"]:
            a = Account(self.client)
            a.values = account
            accounts.append(a)

        return accounts

    def create(self, name):
        pass


class Account(AbstractResource):
    def __call__(self, account_id):
        r = self.client.get("/accounts/" + str(account_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["account"]

        return self

    def delete(self):
        pass

    def edit(self, group_name):
        pass
