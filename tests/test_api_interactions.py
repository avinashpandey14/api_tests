# tests/test_api_interactions.py
import unittest
from api.api_client import APIClient
from config.config import API_URL

class TestAPIInteractions(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient()

    def test_example_api_interaction(self):
        # Example test case for API interaction
        response = self.api_client.get_products(API_URL)
        
        # Add assertions or further test logic based on the API response
        self.assertEqual(response.status_code, 200)  # Example assertion
        
        # Example: Test that the response contains expected data
        data = response.json()
        self.assertTrue('products' in data.keys())

if __name__ == "__main__":
    unittest.main()
