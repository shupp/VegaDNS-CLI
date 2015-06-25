from vegadns_client.common import AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class UpdateData(AbstractResourceCollection):
    def __call__(self):
        r = self.client.get("/update-local-tinydns-data")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        return r.content
