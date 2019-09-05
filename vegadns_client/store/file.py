import json
import md5
import os.path

from vegadns_client.store import AccessTokenStoreAbstract


class AccessTokenStoreFile(AccessTokenStoreAbstract):
    def __init__(
        self,
        key,
        secret,
        host,
        version=1.0,
        directory="~/",
        prefix=".vegadns-access-token-"
    ):
        super(AccessTokenStoreFile, self).__init__(
            key, secret, host, version
        )
        hash = md5.new(key + secret + host).hexdigest()
        self.token_file = os.path.expanduser(directory + prefix + hash)

    def get(self):
        if not os.path.exists(self.token_file):
            return None

        with open(self.token_file) as token_file:
            data = json.load(token_file)
            if data.get('expires_at', 0) < self.now:
                return None
            return data['access_token']

    def get_expires_at(self):
        if not os.path.exists(self.token_file):
            return None

        with open(self.token_file) as token_file:
            data = json.load(token_file)
            if data.get('expires_at', 0) < self.now:
                return None
            return data['expires_at']

    def save(self, access_token, expires_in):
        newdata = {
            'access_token': access_token,
            'expires_at': self.now + expires_in
        }

        with os.fdopen(
            os.open(self.token_file, os.O_WRONLY | os.O_CREAT, 0o600),
            'w'
        ) as token_file:

            json.dump(newdata, token_file)
