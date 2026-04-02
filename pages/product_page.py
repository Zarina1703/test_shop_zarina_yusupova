from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def click_terms_and_conditions_button(self):
        self.find(loc.terms_and_conditions_loc).click()

    def icon_of_facebook_is_displayed(self):
        self.check_element_is_displayed(loc.icon_of_facebook)

    def get_page_title(self):
        return self.get_text(loc.page_title)


