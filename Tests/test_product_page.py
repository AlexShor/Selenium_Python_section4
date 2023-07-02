from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('parameter', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(4)])
def test_guest_can_add_product_to_basket(browser, parameter):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{parameter}"
    page = ProductPage(browser, link, 5)
    page.open()
    page.add_product_to_basket()
    page.product_should_be_added_to_basket()




