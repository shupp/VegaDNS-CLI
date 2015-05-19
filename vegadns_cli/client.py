import json
import time
import os.path
import logging
import requests
from requests import auth


logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, host, access_token=None):
        self.host = host
        self.access_token = access_token

    def get(self, path):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        return requests.get(self.host + path, headers=headers)


class AccessToken:
    def __init__(self, environment, config):
        self.environment = environment
        self.key = config.get(environment, 'key')
        self.secret = config.get(environment, 'secret')
        self.host = config.get(environment, 'host')
        self.token_file = os.path.expanduser(
            '~/.vegadns-access-token-' + self.environment
        )
        self.now = int(time.time())
        self.access_token = self.get_access_token()

    def get_access_token(self):
        token = self.get_access_token_from_local()
        if token is None:
            newdata = self.get_access_token_from_api(
                self.key,
                self.secret,
                self.host
            )
            self.save_access_token(newdata)
            return newdata['access_token']
        else:
            return token

    def save_access_token(self, data):
        newdata = {
            'access_token': data['access_token'],
            'expires_at': self.now + data['expires_in']
        }
        with open(self.token_file, 'w') as token_file:
            json.dump(newdata, token_file)

    def get_access_token_from_local(self):
        if not os.path.exists(self.token_file):
            return None

        with open(self.token_file) as token_file:
            data = json.load(token_file)
            if data.get('expires_at', 0) < self.now:
                return None
            return data['access_token']

    def get_access_token_from_api(self, key, secret, host):
        r = requests.post(
            host + "/token",
            auth=auth.HTTPBasicAuth(key, secret),
            data={"grant_type": "client_credentials"}
        )
        if r.status_code != 200:
            # FIXME error handling
            raise Exception("Error fetching token: " + str(r.status_code))

        return r.json()
