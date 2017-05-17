from apiwrapper.endpoints.master_card_action import MasterCardAction
from apiwrapper.tests.endpoints.test_endpoint import EndpointTest


class MasterCardActionTest(EndpointTest):

    def setUp(self):
        super().setUp(MasterCardAction)

    def test_get_base_endpoint(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/mastercard-action" % (
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_base_endpoint(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_all_master_card_actions_for_account(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/mastercard-action" % (
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_all_master_card_actions_for_account(
            self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)

    def test_get_master_card_action_by_id(self):
        endpoint_should_be = "/user/%d/monetary-account/%d" \
                             "/mastercard-action/%d" % (
                                 self.random_id,
                                 self.random_id,
                                 self.random_id
                             )
        endpoint_to_check = self.test_class.get_master_card_action_by_id(
            self.random_id, self.random_id, self.random_id)
        self.assert_parameters(endpoint_should_be, endpoint_to_check)
