from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.header import Header


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.header = Header(driver)

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        return self.find(locator).text.strip()

    def clear_text(self, text):
        return text.strip()

    def check_title_is(self, title):
        assert self.driver.title == title

    def check_element_is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def clean_price(self, price):
        return float(price.replace(",", "").strip())

    def get_price(self, locator):
        return self.clean_price(self.get_text(locator))

    def wait_for_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_for_invisible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def check_that_default_state_of_checkboxes_is_unchecked(self, list_of_checkboxes):
        for item in list_of_checkboxes:
            assert item.get_attribute("checked") is None

    def check_current_url_is(self, current_url):
        assert self.driver.current_url == current_url

    def wait_for_inner_text_is(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(
            lambda d: self.find(locator).get_attribute('innerText') == str(text)
        )

    def wait_for_current_url_is(self, current_url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(current_url))
