from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def product_should_be_added_to_basket(self):
        self.should_be_alert_success()
        self.should_be_alert_basket_total_price()

    def should_be_alert_success(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        success_alerts = [elem.text for elem in self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS_INNER)]
        assert product_title in ''.join(success_alerts), 'Alert with product title not presented or wrong title'

    def should_be_alert_basket_total_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_basket_total_texts = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text
        assert product_price in alert_basket_total_texts, 'Alert with basket total price not presented or wrong price'
