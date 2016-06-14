from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class LocationPrefixes(AbstractResourceCollection):
    def __call__(self, location_id):
        query_params = {"location_id": location_id}

        r = self.client.get("/location_prefixes", query_params)
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        location_prefixes = []
        for prefix in decoded["location_prefixes"]:
            r = LocationPrefix(self.client)
            r.values = prefix
            location_prefixes.append(r)

        return location_prefixes

    def create(self, data):
        r = self.client.post(
            "/location_prefixes",
            data=data
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = LocatoinPrefix(self.client)
        m.values = decoded["location_prefix"]

        return m


class LocationPrefix(AbstractResource):
    def __call__(self, prefix_id):
        r = self.client.get("/location_prefixes/" + str(prefix_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["location_prefix"]

        return self

    def delete(self):
        # make sure we have a prefix_id set
        if self.values.get('prefix_id', False) is False:
            raise ClientException(400, "prefix_id is not set")

        r = self.client.delete(
            "/location_prefixes/" + str(self.values["prefix_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, data):
        r = self.client.put(
            "/location_prefixes/" + str(self.values["prefix_id"]),
            data=data
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = LocationPrefix(self.client)
        m.values = decoded["location_prefix"]

        return m
