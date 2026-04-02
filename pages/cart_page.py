from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    def empty_cart_message(self):
        return self.get_text(loc.empty_cart_message_loc)

    def check_review_order_is_displayed(self):
        assert self.check_element_is_displayed(loc.review_order_loc)
