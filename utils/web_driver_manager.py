# utils/webdriver_manager.py
from selenium import webdriver

def get_safari_driver():
    # Initialize Safari WebDriver
    driver = webdriver.Safari()
    driver.maximize_window()
    return driver
