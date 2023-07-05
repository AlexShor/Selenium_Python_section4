import time

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.constants.urls import FullDomains


@pytest.mark.go_to_login_page
def test_guest_can_go_to_login_page(browser):
    link = FullDomains.SELEN_PY_COM
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.see_product_in_basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = FullDomains.SELEN_PY_COM
    page = MainPage(browser, link, 5)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()
