from vegadns_client.common import AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class ReleaseVersion(AbstractResourceCollection):
    def __call__(self):
        r = self.client.get("/release_version")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        return decoded['release_version']
