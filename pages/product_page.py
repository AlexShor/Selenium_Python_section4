from .base_page import BasePage
from .constants.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self, solve_quiz=False):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        if solve_quiz:
            self.solve_quiz_and_get_code()

    def product_should_be_added_to_basket(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.should_be_alert_success(product_title)
        self.should_be_alert_basket_total_price(product_price)
        self.should_be_basket_total_price(product_price)

    def should_be_alert_success(self, product_title):
        success_alerts = [elem.text for elem in self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS_INNER)]
        check = False
        for strong_text in success_alerts:
            if strong_text == product_title:
                check = True
        assert check, 'Alert with product title not presented or wrong title'

    def should_be_alert_basket_total_price(self, product_price):
        alert_basket_total_texts = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text
        assert product_price == alert_basket_total_texts, 'Alert with basket total price not presented or wrong price'

    def should_be_basket_total_price(self, product_price):
        basket_total_price_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert product_price in basket_total_price_text, 'Basket total price not presented or wrong price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_INNER), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_INNER), \
            "Success message is presented, but should have disappeared"
