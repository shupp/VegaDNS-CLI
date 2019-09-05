from builtins import str
from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class DefaultRecords(AbstractResourceCollection):
    def __call__(self, filter=None):
        # filter will be supported later
        r = self.client.get("/default_records")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        records = []
        for record in decoded["default_records"]:
            r = DefaultRecord(self.client)
            r.values = record
            records.append(r)

        return records

    def create(self, data):
        r = self.client.post(
            "/default_records",
            data=data
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = DefaultRecord(self.client)
        m.values = decoded["default_record"]

        return m


class DefaultRecord(AbstractResource):
    def __call__(self, record_id):
        r = self.client.get("/default_records/" + str(record_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["default_record"]

        return self

    def delete(self):
        # make sure we have a record_id set
        if self.values.get('record_id', False) is False:
            raise ClientException(400, "record_id is not set")

        r = self.client.delete(
            "/default_records/" + str(self.values["record_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, data):
        r = self.client.put(
            "/default_records/" + str(self.values["record_id"]),
            data=data
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = DefaultRecord(self.client)
        m.values = decoded["default_record"]

        return m
