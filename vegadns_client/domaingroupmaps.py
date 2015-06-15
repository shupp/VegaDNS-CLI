from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class DomainGroupMaps(AbstractResourceCollection):
    def __call__(self, domain_id, filter=None):
        # filter will be supported later
        r = self.client.get("/domaingroupmaps?domain_id=" + domain_id)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        maps = []
        for map in decoded["domaingroupmaps"]:
            m = DomainGroupMap(self.client)
            m.values = map
            maps.append(m)

        return maps

    def create(self, domain_id, group_id,
               can_read=1, can_write=1, can_delete=1):

        r = self.client.post(
            "/domaingroupmaps",
            data={
                'domain_id': domain_id,
                'group_id': group_id,
                'can_read': can_read,
                'can_write': can_write,
                'can_delete': can_delete
            }
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = DomainGroupMap(self.client)
        m.values = decoded["domaingroupmap"]

        return m


class DomainGroupMap(AbstractResource):
    def __call__(self, map_id):
        r = self.client.get("/domaingroupmaps/" + map_id)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["domaingroupmap"]

        return self

    def delete(self):
        # make sure we have a group_id set
        if self.values.get('map_id', False) is False:
            raise ClientException(400, "map_id is not set")

        r = self.client.delete(
            "/domaingroupmaps/" + str(self.values["map_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, can_read, can_write, can_delete):
        if self.values.get('map_id', False) is False:
            raise ClientException(400, "map_id is not set")

        r = self.client.put(
            "/domaingroupmaps/" + str(self.values["map_id"]),
            data={
                'can_read': can_read,
                'can_write': can_write,
                'can_delete': can_delete
            }
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["domaingroupmap"]

        return self
