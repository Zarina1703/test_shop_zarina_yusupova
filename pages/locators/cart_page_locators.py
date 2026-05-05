from selenium.webdriver.common.by import By

empty_cart_message_loc = (By.CSS_SELECTOR, '.js_cart_lines')
review_order_loc = (By.CSS_SELECTOR, '.d-md-flex:nth-child(1)')
shipping_loc = (By.CSS_SELECTOR, '.d-md-flex:nth-child(2)')
payment_loc = (By.CSS_SELECTOR, '.d-md-flex:nth-child(3)')
list_of_remove_one_button_loc = (By.CSS_SELECTOR, '[aria-label="Remove one"]')
list_of_add_one_button_loc = (By.CSS_SELECTOR, '[aria-label="Add one"]')
list_value_of_product_loc = (By.CSS_SELECTOR, '.js_quantity')
list_of_product_prices_loc = (By.CSS_SELECTOR, '[data-oe-expression="product_price"] span')
subtotal_price_loc = (By.CSS_SELECTOR, '#order_total_untaxed span span')
