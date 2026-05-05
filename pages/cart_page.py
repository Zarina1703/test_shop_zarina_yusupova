from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc
from pages.locators import common_locators as common_loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    def check_for_empty_cart_message(self):
        assert self.get_text(loc.empty_cart_message_loc) == 'Your cart is empty!'

    def check_review_order_is_displayed(self):
        assert self.check_element_is_displayed(loc.review_order_loc)

    def remove_one_position_from_cart(self, index=0):
        self.find_all(loc.list_of_remove_one_button_loc)[index].click()

    def add_one_position_to_cart(self, index=0, expected_value=2):
        self.find_all(loc.list_of_add_one_button_loc)[index].click()

    def check_that_count_of_product_in_cart_is(self, count):
        assert self.wait_for_inner_text_is(common_loc.count_of_product_in_cart_loc, count)

    def check_that_value_of_product_is(self, index_of_product, value_of_product):
        value = self.find_all(loc.list_value_of_product_loc)[index_of_product].get_attribute('value')
        assert int(value) == value_of_product

    def check_that_product_price_is_correct(self, index_of_product, expected_price):
        price = self.clean_price(self.find_all(loc.list_of_product_prices_loc)[index_of_product].text)
        assert expected_price == price


    def check_that_subtotal_price_in_cart_is_correct(self):
        prices_of_product = [self.clean_price(p.text) for p in self.find_all(loc.list_of_product_prices_loc)]
        assert sum(prices_of_product) == self.get_price(loc.subtotal_price_loc)
