class AbstractResource(object):
    def __init__(self, client):
        self.client = client


class AbstractResourceCollection(object):
    def __init__(self, client):
        self.client = client
        self.values = {}
