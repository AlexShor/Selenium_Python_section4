import time

import pytest
from faker import Faker

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.constants.urls import Links, QueryParams


@pytest.mark.registered_user_add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Links.LOGIN_PAGE_URL)
        page.open()
        page.register_new_user(Faker().email(), "Aaa123123123")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Links.BOOK_CODERS_AT_WORK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Links.BOOK_CODERS_AT_WORK)
        page.open()
        page.add_product_to_basket()
        page.product_should_be_added_to_basket()


@pytest.mark.need_review
@pytest.mark.add_product_to_basket
@pytest.mark.parametrize('param', [
    pytest.param('offer' + str(i), marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"{Links.BOOK_CODERS_AT_WORK}?{QueryParams.PROMO}={param}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket(True)
    page.product_should_be_added_to_basket()
    time.sleep(3)


@pytest.mark.display_disappear_messages
@pytest.mark.skip(reason='Not actual feature')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.BOOK_CODERS_AT_WORK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.display_disappear_messages
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.BOOK_CODERS_AT_WORK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.display_disappear_messages
@pytest.mark.skip(reason='Not actual feature')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.BOOK_CODERS_AT_WORK)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()


@pytest.mark.go_to_login_page
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Links.BOOK_THE_CITY_AND_THE_STARS)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.go_to_login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Links.BOOK_THE_CITY_AND_THE_STARS)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.see_product_in_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Links.BOOK_CODERS_AT_WORK
    page = ProductPage(browser, link, 5)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()
