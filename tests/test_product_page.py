def test_check_functional_of_terms_and_conditionals_button(product_page):
    product_page.open_page()
    product_page.click_terms_and_conditions_button()
    assert product_page.get_current_url() == "http://testshop.qa-practice.com/terms"


def test_check_icon_of_facebook_is_displayed(product_page):
    product_page.open_page()
    product_page.icon_of_facebook_is_displayed()


def test_check_that_page_title_is_correct(product_page):
    product_page.open_page()
    assert product_page.get_page_title() == 'Office Design Software'
