from endpoints.user import User


class Card(User):

    endpoint_card = "card"

    @classmethod
    def get_base_endpoint(cls, user_id):
        endpoint = User.get_base_endpoint(user_id)
        endpoint += "/%s" % cls.endpoint_card
        return endpoint

    def get_all_cards_for_user(self, user_id):
        endpoint = self.get_base_endpoint(user_id)

        return self.__make_get_request(endpoint)

    def get_card_for_user_by_id(self, user_id, card_id):
        endpoint = self.get_base_endpoint(user_id)
        endpoint += "/%d" % card_id

        return self.__make_get_request(endpoint)
