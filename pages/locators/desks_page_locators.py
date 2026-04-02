from selenium.webdriver.common.by import By


sort_by_loc = (By.CSS_SELECTOR, '.o_sortby_dropdown > a')
sort_by_low_to_high_loc = (By.CSS_SELECTOR, '.dropdown-menu > a:nth-child(4)')
sort_by_high_to_low_loc = (By.CSS_SELECTOR, '.dropdown-menu > a:nth-child(5)')
sort_by_name_loc = (By.CSS_SELECTOR, '.dropdown-menu > a:nth-child(3)')
list_of_prices_loc = (By.CSS_SELECTOR, '.oe_currency_value')
list_of_names_loc = (By.CSS_SELECTOR, 'h6 > a')
list_of_checkboxes_loc = (By.CSS_SELECTOR, '#o_products_attributes_1 input')