# api/api_client.py
import requests

class APIClient:
    def get_products(self, url):
        return requests.get(url)
