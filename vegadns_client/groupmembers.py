from builtins import str
from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class GroupMembers(AbstractResourceCollection):
    def __call__(self, group_id, filter=None):
        # filter will be supported later
        r = self.client.get("/groupmembers?group_id=" + str(group_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        members = []
        for member in decoded["groupmembers"]:
            m = GroupMember(self.client)
            m.values = member
            members.append(m)

        return members

    def create(self, group_id, account_id, is_admin=0):
        r = self.client.post(
            "/groupmembers",
            data={
                'group_id': group_id,
                'account_id': account_id,
                'is_admin': is_admin
            }
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        g = GroupMember(self.client)
        g.values = decoded["groupmember"]

        return g


class GroupMember(AbstractResource):
    def __call__(self, groupmember_id):
        r = self.client.get("/groupmembers/" + str(groupmember_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["groupmember"]

        return self

    def delete(self):
        # make sure we have a group_id set
        if self.values.get('member_id', False) is False:
            raise ClientException(400, "groupmember_id is not set")

        r = self.client.delete(
            "/groupmembers/" + str(self.values["member_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, is_admin):
        if self.values.get('member_id', False) is False:
            raise ClientException(400, "member_id is not set")
        if self.values.get('is_admin', False) is False:
            raise ClientException(400, "is_admin is not set")

        r = self.client.put(
            "/groupmembers/" + str(self.values["member_id"]),
            data={'is_admin': is_admin}
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)
