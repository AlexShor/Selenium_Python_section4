from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 5)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
