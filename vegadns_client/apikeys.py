from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class ApiKeys(AbstractResourceCollection):
    def __call__(self, account_ids=None):
        if account_ids is not None:
            r = self.client.get(
                "/apikeys",
                params={"account_ids": account_ids}
            )
        else:
            r = self.client.get("/apikeys")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        apikeys = []
        for apikey in decoded["apikeys"]:
            a = ApiKey(self.client)
            a.values = apikey
            apikeys.append(a)

        return apikeys

    def create(self, data):
        r = self.client.post(
            "/apikeys",
            data=data
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = ApiKey(self.client)
        m.values = decoded["apikey"]

        return m


class ApiKey(AbstractResource):
    def __call__(self, apikey_id):
        r = self.client.get("/apikeys/" + str(apikey_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["apikey"]

        return self

    def delete(self):
        if self.values.get('apikey_id', False) is False:
            raise ClientException(400, "apikey_id is not set")

        r = self.client.delete(
            "/apikeys/" + str(self.values["apikey_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, data):
        if self.values.get('apikey_id', False) is False:
            raise ClientException(400, "apikey_id is not set")

        r = self.client.put(
            "/apikeys/" + str(self.values["apikey_id"]),
            data=data
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["apikey"]

        return self
