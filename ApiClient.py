import requests

class ApiClient:

    api_version = 1
    uri = f"https://api.bunq.com/v{api_version}"

    def get(self, endpoint):


