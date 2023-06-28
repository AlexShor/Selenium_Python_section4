import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_display_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)

    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
