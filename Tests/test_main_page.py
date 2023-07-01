import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_display_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(2)
    go_to_login_page(browser)

    time.sleep(2)
