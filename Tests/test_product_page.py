from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.add_product_to_basket
@pytest.mark.parametrize('parameter', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(1)])
def test_guest_can_add_product_to_basket(browser, parameter):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{parameter}"
    page = ProductPage(browser, link, 5)
    page.open()
    page.add_product_to_basket()
    page.product_should_be_added_to_basket()


@pytest.mark.display_disappear_messages
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link, 5)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.display_disappear_messages
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link, 5)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.display_disappear_messages
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link, 5)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()



