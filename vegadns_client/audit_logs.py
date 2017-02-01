from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class AuditLogs(AbstractResourceCollection):
    def __call__(self, domain_ids=None, sort=None, order=None, search=None):
        params = {}
        if domain_ids is not None:
            params["domain_ids"] = domain_ids
        if sort is not None:
            params["sort"] = sort
        if order is not None:
            params["order"] = order
        if search is not None:
            params["search"] = search

        r = self.client.get(
            "/audit_logs",
            params=params
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        audit_logs = []
        for audit_log in decoded["audit_logs"]:
            a = AuditLog(self.client)
            a.values = audit_log
            audit_logs.append(a)

        return audit_logs


class AuditLog(AbstractResource):
    pass
