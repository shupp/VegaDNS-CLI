from vegadns_client.common import AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Export(AbstractResourceCollection):
    def __call__(self, format="tinydns", filter=None):
        # filter will be supported later
        r = self.client.get("/export/" + format)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        return r.content
