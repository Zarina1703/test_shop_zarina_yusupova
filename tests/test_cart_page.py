def test_empty_cart_message(cart_page):
    cart_page.open_page()
    assert cart_page.empty_cart_message() == 'Your cart is empty!'


def test_title(cart_page):
    cart_page.open_page()
    assert cart_page.check_title_is() == 'Shopping Cart | My Website'


def test_review_order(cart_page):
    cart_page.open_page()
    cart_page.check_review_order_is_displayed()
