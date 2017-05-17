from apiwrapper.endpoints.device import Device
from apiwrapper.tests.endpoints.test_endpoint import EndpointTest


class DeviceTest(EndpointTest):

    def setUp(self):
        super().setUp(Device)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/device"
        endpoint_to_check = self.test_class._get_base_endpoint()
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_device_by_id(self):
        endpoint_should_be = "/device/%d" % self.random_id
        endpoint_to_check = self.test_class.get_device_by_id(self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)
