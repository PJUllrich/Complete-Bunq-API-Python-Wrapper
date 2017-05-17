from apiwrapper.endpoints.request_inquiry import RequestInquiry
from apiwrapper.tests.endpoints.test_endpoint import EndpointTest


class RequestInquiryTest(EndpointTest):
    def setUp(self):
        super().setUp(RequestInquiry)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" % (
            self.random_id,
            self.random_id
        )
        endpoint_to_check = self.test_class._get_base_endpoint(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_inquiries_for_account(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-inquiry" % (
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_all_inquiries_for_account(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_request_inquiry_by_id(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-inquiry/%d" % (
                                 self.random_id,
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_request_inquiry_by_id(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_chat_for_request_inquiry(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-inquiry/%d/chat" % (
                                 self.random_id,
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_chat_for_request_inquiry(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_batch_inquiries_for_account(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-inquiry-batch" % (
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_all_batch_inquiries_for_account(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_batch_inquiry_by_id(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-inquiry-batch/%d" % (
                                 self.random_id,
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_batch_inquiry_by_id(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_request_responses_for_account(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-response" % (
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_all_request_responses_for_account(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_request_response_by_id(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-response/%d" % (
                                 self.random_id,
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_request_response_by_id(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_chat_for_request_response(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/request-response/%d/chat" % (
                                 self.random_id,
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_chat_for_request_response(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)
