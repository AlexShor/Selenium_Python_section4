import time
from math import log, sin

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from .constants.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def is_element_present(self, method, css_selector):
        try:
            self.browser.find_element(method, css_selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON).click()

    def get_page_language(self):
        return self.browser.find_element(*BasePageLocators.HTML).get_attribute("lang")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}", end=' ')
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented", end=' ')
        finally:
            if 'firefox' in str(self.browser): time.sleep(1)
