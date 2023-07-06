from .base_page import BasePage
from .constants.locators import BasketPageLocators, BasePageLocators
from .constants.urls import Pages
from .constants.translated_elements import BasketPageTranslateElements


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_page_url()
        self.should_be_title_basket_page()
        self.should_be_breadcrumb_basket_page()

    def should_be_basket_page_url(self):
        assert f'/{Pages.BASKET}/' in self.browser.current_url, f"Current url in not {Pages.BASKET} page url"

    def should_be_title_basket_page(self):
        translate_basket = BasketPageTranslateElements.BASKET.get(self.get_page_language()).lower()
        page_title = self.browser.find_element(*BasketPageLocators.TITLE_BASKET_PAGE).text.lower()
        assert page_title == translate_basket, f"Current title page in not {translate_basket}"

    def should_be_breadcrumb_basket_page(self):
        translate_basket = BasketPageTranslateElements.BASKET.get(self.get_page_language()).lower()
        active_breadcrumb = self.browser.find_element(*BasePageLocators.ACTIVE_BREADCRUMB).text.lower()
        assert active_breadcrumb == translate_basket, f"Current breadcrumb in not {translate_basket}"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS, 2), \
            "Items in basket is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented, but should be"
