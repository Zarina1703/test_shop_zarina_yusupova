from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header:
    def __init__(self, driver):
        self.driver = driver

    def check_logo_is_enabled(self):
        assert self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Main"]  img').is_enabled()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Main"] .fa.fa-shopping-cart').click()
