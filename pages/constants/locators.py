from selenium.webdriver.common.by import By


class BasePageLocators:
    HTML = (By.TAG_NAME, 'html')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
    ACTIVE_BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb .active")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form button.btn-lg")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".register_form button.btn-lg")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_SUCCESS_INNER = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")


class BasketPageLocators:
    TITLE_BASKET_PAGE = (By.CSS_SELECTOR, ".page-header > h1")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > .basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
