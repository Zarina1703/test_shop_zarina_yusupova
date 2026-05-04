from time import sleep

from pages.base_page import BasePage
from pages.locators import home_page_locators as loc
from selenium.webdriver import ActionChains


class HomePage(BasePage):
    page_url = '/shop'

    def click_first_image_of_product(self):
        self.find_all(loc.list_of_images_loc)[0].click()

    def click_continue_shopping_button(self, expected_count=1):
        self.find(loc.continue_shopping_button_loc).click()
        self.wait_for_inner_text_is(loc.count_of_product_in_cart_loc, expected_count)

    # def add_first_product_to_cart(self):
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(self.find_all(loc.list_of_images_loc)[0]).perform()
    #     self.find_all(loc.list_of_icon_of_cart_loc)[0].click()
    #
    # def add_second_product_to_cart(self):
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(self.find_all(loc.list_of_images_loc)[1]).perform()
    #     self.find_all(loc.list_of_icon_of_cart_loc)[0].click()


    def add_product_to_cart_by_index(self, index=0):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_all(loc.list_of_images_loc)[index]).perform()
        self.find_all(loc.list_of_icon_of_cart_loc)[index].click()
