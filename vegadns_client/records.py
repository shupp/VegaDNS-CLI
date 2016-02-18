from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Records(AbstractResourceCollection):
    def __call__(self, domain_id, search_name, search_value, filter=None):
        # filter will be supported later
        query_params = {"domain_id": domain_id}
        if search_name is not False:
            query_params["search_name"] = search_name
        if search_value is not False:
            query_params["search_value"] = search_value

        r = self.client.get("/records", query_params)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        records = []
        for record in decoded["records"]:
            r = Record(self.client)
            r.values = record
            records.append(r)

        return records

    def create(self, data):
        r = self.client.post(
            "/records",
            data=data
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = Record(self.client)
        m.values = decoded["record"]

        return m


class Record(AbstractResource):
    def __call__(self, record_id):
        r = self.client.get("/records/" + str(record_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["record"]

        return self

    def delete(self):
        # make sure we have a record_id set
        if self.values.get('record_id', False) is False:
            raise ClientException(400, "record_id is not set")

        r = self.client.delete("/records/" + str(self.values["record_id"]))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, data):
        r = self.client.put(
            "/records/" + str(self.values["record_id"]),
            data=data
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = Record(self.client)
        m.values = decoded["record"]

        return m
