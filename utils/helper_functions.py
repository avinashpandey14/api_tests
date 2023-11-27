# utils/helper_functions.py

# Add any common helper functions if required
# just for sake i wrote this code because if any thing needed again and again we can use codes from here.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, locator, timeout=10):
    """
    Wait for an element to be clickable and then click on it.
    
    Args:
        driver: WebDriver instance
        locator: Tuple containing locator strategy and locator value (e.g., (By.ID, 'element_id'))
        timeout: Maximum time to wait for the element (default is 10 seconds)
    """
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()
