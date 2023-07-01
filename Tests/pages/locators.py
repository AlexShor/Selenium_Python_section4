from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_SUCCESS_INNER = (By.CSS_SELECTOR, ".alert-success > .alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info > .alertinner")
