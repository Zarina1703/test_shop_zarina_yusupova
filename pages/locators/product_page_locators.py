from selenium.webdriver.common.by import By

terms_and_conditions_loc = (By.CSS_SELECTOR, '#o_product_terms_and_share p a')
icon_of_facebook = (By.CSS_SELECTOR, '[aria-label="Facebook"]')
page_title = (By.CSS_SELECTOR, '#product_details > h1')
plus_button_loc = (By.CSS_SELECTOR, '[aria-label="Add one"]')
add_to_cart_button_loc = (By.CSS_SELECTOR, '#add_to_cart')
product_price_loc = (By.CSS_SELECTOR, '.oe_price span')
selector_of_currency_loc = (By.CSS_SELECTOR, '.o_pricelist_dropdown > a')
eur_currency_loc = (By.CSS_SELECTOR, '.o_pricelist_dropdown div a:nth-child(2)')
price_currency_loc = (By.CSS_SELECTOR, '[itemprop="priceCurrency"]')
