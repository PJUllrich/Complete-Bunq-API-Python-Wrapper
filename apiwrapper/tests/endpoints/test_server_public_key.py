from apiwrapper.endpoints.server_public_key import ServerPublicKey
from apiwrapper.tests.endpoints.test_endpoint import EndpointTest


class ServerPublicKeyTest(EndpointTest):

    def setUp(self):
        super().setUp(ServerPublicKey)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/installation/%d/server-public-key" % (
            self.random_id
        )
        endpoint_to_check = self.test_class._get_base_endpoint(
            self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_server_pubkey_for_installation(self):
        endpoint_should_be = "/installation/%d/server-public-key" % (
            self.random_id
        )
        endpoint_to_check = self.test_class.get_server_pubkey_for_installation(
            self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)
