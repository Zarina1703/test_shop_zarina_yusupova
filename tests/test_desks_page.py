def test_sorting_by_low_to_high(desks_page):
    desks_page.open_page()
    desks_page.select_sorting_by_low_to_high()
    list_of_prices = desks_page.get_item_prices()
    assert list_of_prices == sorted(list_of_prices)