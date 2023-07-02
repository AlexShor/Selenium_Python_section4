from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time

link1 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
query_param_promo = 'promo'


@pytest.mark.add_product_to_basket
@pytest.mark.parametrize('param', [
    pytest.param('offer' + str(i), marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"{link1}?{query_param_promo}={param}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_should_be_added_to_basket()


@pytest.mark.display_disappear_messages
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.display_disappear_messages
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.display_disappear_messages
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()


@pytest.mark.go_to_login_page
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


@pytest.mark.go_to_login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


