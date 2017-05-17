from apiwrapper.endpoints.credential_password_ip import CredentialPasswordIp
from apiwrapper.tests.endpoints.test_endpoint import EndpointTest


class CredentialPasswordIpTest(EndpointTest):

    def setUp(self):
        super().setUp(CredentialPasswordIp)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/user/%d/credential-password-ip" % (
            self.random_id
        )
        endpoint_to_check = self.test_class._get_base_endpoint(
            self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_credentials_for_user(self):
        endpoint_should_be = "/user/%d/credential-password-ip" % (
            self.random_id
        )
        endpoint_to_check = self.test_class.get_all_credentials_for_user(
            self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_credential_by_id(self):
        endpoint_should_be = "/user/%d/credential-password-ip/%d" % (
            self.random_id,
            self.random_id
        )
        endpoint_to_check = self.test_class.get_credential_by_id(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)
