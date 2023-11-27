# tests/test_products_page.py
import unittest
from pages.products_page import ProductsPage
from utils.web_driver_manager import get_safari_driver
from config.config import BASE_URL

class TestProductsPage(unittest.TestCase):
    def setUp(self):
        self.driver = get_safari_driver()
        self.driver.get(BASE_URL)
        self.products_page = ProductsPage(self.driver)

    def test_example(self):
        # Write test cases for interactions with the products page
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
