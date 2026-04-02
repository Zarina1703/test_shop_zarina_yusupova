from selenium.webdriver.common.by import By


class Header:
    def __init__(self, driver):
        self.driver = driver

    def check_logo_is_enabled(self):
        assert self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Main"]  img').is_enabled()
