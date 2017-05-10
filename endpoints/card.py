from endpoints.endpoint import Endpoint


class Card(Endpoint):

    def get_base_endpoint(self, user_id):
        return "%s/%d/%s" % (
            self.endpoint_user,
            user_id,
            self.endpoint_card
        )

    def get_all_cards_for_user(self, user_id):
        endpoint = self.get_base_endpoint(user_id)

        return self.make_get_request(endpoint)

    def get_card_for_user_by_id(self, user_id, card_id):
        endpoint = self.get_base_endpoint(user_id)
        endpoint += "/%d" % card_id

        return self.make_get_request(endpoint)
