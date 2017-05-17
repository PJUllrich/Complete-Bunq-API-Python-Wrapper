from apiwrapper.endpoints.permitted_ip import PermittedIp
from apiwrapper.tests.endpoints.test_endpoint import EndpointTest


class PermittedIpTest(EndpointTest):

    def setUp(self):
        super().setUp(PermittedIp)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/user/%d/credential-password-ip/%d/ip" % (
            self.random_id,
            self.random_id
        )
        endpoint_to_check = self.test_class._get_base_endpoint(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_permitted_ip(self):
        endpoint_should_be = "/user/%d/credential-password-ip/%d/ip" % (
            self.random_id,
            self.random_id
        )
        endpoint_to_check = self.test_class.get_all_permitted_ip(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_permitted_ip_by_id(self):
        endpoint_should_be = "/user/%d/credential-password-ip/%d/ip/%d" % (
            self.random_id,
            self.random_id,
            self.random_id
        )
        endpoint_to_check = self.test_class.get_permitted_ip_by_id(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)
