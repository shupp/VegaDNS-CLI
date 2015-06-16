from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Groups(AbstractResourceCollection):
    def __call__(self, filter=None):
        # filter will be supported later
        r = self.client.get("/groups")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        groups = []
        for group in decoded["groups"]:
            g = Group(self.client)
            g.values = group
            groups.append(g)

        return groups

    def create(self, name):
        r = self.client.post("/groups", data={'name': name})
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        g = Group(self.client)
        g.values = decoded["group"]

        return g


class Group(AbstractResource):
    def __call__(self, group_id):
        r = self.client.get("/groups/" + str(group_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["group"]

        return self

    def delete(self):
        # make sure we have a group_id set
        if self.values.get('group_id', False) is False:
            raise ClientException(400, "group_id is not set")

        r = self.client.delete("/groups/" + str(self.values["group_id"]))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, group_name):
        pass
