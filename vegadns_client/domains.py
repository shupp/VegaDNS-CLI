from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Domains(AbstractResourceCollection):
    def __call__(self, filter=None):
        # filter will be supported later
        r = self.client.get("/domains")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        domains = []
        for domain in decoded["domains"]:
            d = Domain(self.client)
            d.values = domain
            domains.append(d)

        return domains

    def create(self, name):
        pass


class Domain(AbstractResource):
    def __call__(self, domain_id):
        r = self.client.get("/domains/" + domain_id)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["domain"]

        return self

    def delete(self):
        pass

    def edit(self, group_name):
        pass
