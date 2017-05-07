import base64
import json

import requests
import uuid

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from config import Controller


class ApiClient:

    __version_api = 1
    __version = '0.0.1'
    __request_id = str(uuid.uuid1())
    __uri = f"https://api.bunq.com/v{__version_api}"

    def __init__(self):
        self.config = Controller()

    def get(self, endpoint, verify=False):
        pass

    def post(self, endpoint, payload):
        action = 'POST /v%d/%s' % (self.__version_api, endpoint)
        msg = self.create_message(action, payload)

        headers = self.headers.copy()
        headers['X-Bunq-Client-Signature'] = self.sign(msg)
        url = '%s/%s' % (self.__uri, endpoint)

        return requests.request('POST', url, headers=headers, json=payload)

    def create_message(self, action, payload):
        headers_as_text = '\n'.join(['%s: %s' % (k, v) for k, v in sorted(
                self.headers.items())])
        msg = '%s\n%s\n\n' % (action, headers_as_text)

        if payload:
            msg += json.dumps(payload)

        return msg

    def sign(self, msg):
        """Create signature for message
        Taken from https://github.com/madeddie/python-bunq - Thanks!

        :param msg: data to be signed, usually action, headers and body
        :type msg: str

        """
        return base64.b64encode(
            self.privkey.sign(
                msg.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        ).decode()

    def verify(self, res):
        """Verify response from server
        Taken from https://github.com/madeddie/python-bunq - Thanks!

        :param res: request to be verified
        :type res: requests.models.Response

        """
        if not self.server_pubkey:
            print('No server public key defined, skipping verification')
            return

        serv_headers = [
            'X-Bunq-Client-Request-Id',
            'X-Bunq-Client-Response-Id'
        ]

        msg = '%s\n%s\n\n%s' % (
            res.status_code,
            '\n'.join(
                ['%s: %s' % (k, v) for k, v in sorted(
                    res.headers.items()
                ) if k in serv_headers]
            ),
            res.text
        )

        signature = base64.b64decode(res.headers['X-Bunq-Server-Signature'])

        try:
            self.server_pubkey.verify(
                signature,
                msg.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except InvalidSignature:
            print('Message failed verification, data might be tampered with')
            return False
        else:
            return True

    @property
    def headers(self):
        headers = {
            'Cache-Control': 'no-cache',
            'User-Agent': 'universal-bunq-api-python/' + self.__version,
            'X-Bunq-Client-Request-Id': self.__request_id,
            'X-Bunq-Geolocation': '0 0 0 0 NL',
            'X-Bunq-Language': 'en_US',
            'X-Bunq-Region': 'nl_NL'
        }
        if self.user_token:
            headers['X-Bunq-Client-Authentication'] = self.server_token

        return headers

    @property
    def user_token(self):
        return self.config.get('user_token')

    @property
    def server_token(self):
        return self.config.get('server_token')

    @property
    def pubkey(self):
        return self.config.get('key_public')

    @property
    def privkey(self):
        return self.config.get('key_private')

    @property
    def api_key(self):
        return self.config.get('api_key')

    @property
    def server_pubkey(self):
        return self.config.get('server_pubkey')


