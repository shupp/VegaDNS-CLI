from builtins import str
from vegadns_client.common import AbstractResource, AbstractResourceCollection
from vegadns_client.exceptions import ClientException


class Locations(AbstractResourceCollection):
    def __call__(self):
        r = self.client.get("/locations")
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        locations = []
        for location in decoded["locations"]:
            l = Location(self.client)
            l.values = location
            locations.append(l)

        return locations

    def create(self, data):
        r = self.client.post(
            "/locations",
            data=data
        )
        if r.status_code != 201:
            raise ClientException(r.status_code, r.content)
        decoded = r.json()
        m = Location(self.client)
        m.values = decoded["location"]

        return m


class Location(AbstractResource):
    def __call__(self, location_id):
        r = self.client.get("/locations/" + str(location_id))
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["location"]

        return self

    def delete(self):
        if self.values.get('location_id', False) is False:
            raise ClientException(400, "location_id is not set")

        r = self.client.delete(
            "/locations/" + str(self.values["location_id"])
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

    def edit(self, data):
        if self.values.get('location_id', False) is False:
            raise ClientException(400, "location_id is not set")

        r = self.client.put(
            "/locations/" + str(self.values["location_id"]),
            data=data
        )
        if r.status_code != 200:
            raise ClientException(r.status_code, r.content)

        decoded = r.json()
        self.values = decoded["location"]

        return self
