from selenium import webdriver
import pytest
from pages.cart_page import CartPage
from pages.desks_page import DesksPage
from pages.product_page import ProductPage
from pages.home_page import HomePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    return chrome_driver


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def desks_page(driver):
    return DesksPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture()
def home_page(driver):
    return HomePage(driver)