from cryptography.hazmat.primitives import serialization

from api_clients.api_client import ApiClient


class ApiClientNonPersisting(ApiClient):

    def __init__(self, privkey, api_key, user_token=None, session_token=None,
                 server_pubkey=None):
        super().__init__()
        self.__privkey = privkey
        self.__user_token = user_token
        self.__session_token = session_token
        self.__server_pubkey = server_pubkey
        self.__api_key = api_key

    def set_session_token(self, token):
        self.__session_token = token

    def set_user_token(self, token):
        self.__user_token = token

    @property
    def user_token(self):
        return self.__user_token

    @user_token.setter
    def user_token(self, value):
        self.__user_token = value

    @property
    def server_token(self):
        return None

    @property
    def session_token(self):
        return self.__session_token

    @session_token.setter
    def session_token(self, value):
        self.__session_token = value

    @property
    def pubkey(self):
        return self.privkey_pem.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @property
    def privkey(self):
        return self.__privkey

    @property
    def api_key(self):
        return self.__api_key

    @property
    def server_pubkey(self):
        return self.__server_pubkey

    @server_pubkey.setter
    def server_pubkey(self, value):
        self.__server_pubkey = value

