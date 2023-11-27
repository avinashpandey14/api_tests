"""
# pages/products_page.py
from .base_page import BasePage

class ProductsPage(BasePage):
    # Define locators or methods specific to the products page
    pass  # Add methods for interactions with elements on the products page

"""
from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    # Locators
    PRODUCT_LIST = (By.CLASS_NAME, 'product-list')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'add-to-cart-button')
    CART_ICON = (By.CLASS_NAME, 'cart-icon')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://dummyjson.com/docs/products")  # Replace with actual URL

    def get_product_list(self):
        return self.driver.find_element(*self.PRODUCT_LIST)

    def add_product_to_cart(self):
        product_list = self.get_product_list()
        add_to_cart_buttons = product_list.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()  # Click the first "Add to Cart" button

    def navigate_to_cart(self):
        cart_icon = self.wait_for_element(self.CART_ICON)
        cart_icon.click()
        # Add logic to navigate to the cart page after clicking the cart icon
        # You can return a new page object representing the cart page here if needed
