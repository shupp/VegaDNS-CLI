from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Records(AbstractResourceCollection):
    def __call__(self, domain_id, filter=None):
        # filter will be supported later
        r = self.client.get("/records?domain_id=" + str(domain_id))
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
        pass

    def edit(self, group_name):
        pass
