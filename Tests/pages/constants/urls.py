class FullDomains:
    SELEN_PY_COM = 'http://selenium1py.pythonanywhere.com'


class Paths:
    CATALOGUE = 'catalogue'
    ACCOUNTS = 'accounts'


class Pages:
    BOOK_1 = 'coders-at-work_207'
    BOOK_2 = 'the-city-and-the-stars_95'
    LOGIN = 'login'
    BASKET = 'basket'


class Links(FullDomains, Paths):
    BOOK_CODERS_AT_WORK = f'{FullDomains.SELEN_PY_COM}/{Paths.CATALOGUE}/{Pages.BOOK_1}/'
    BOOK_THE_CITY_AND_THE_STARS = f'{FullDomains.SELEN_PY_COM}/{Paths.CATALOGUE}/{Pages.BOOK_2}/'
    LOGIN_PAGE_URL = f'{FullDomains.SELEN_PY_COM}/{Paths.ACCOUNTS}/{Pages.LOGIN}/'
    BASKET_PAGE_URL = f'{FullDomains.SELEN_PY_COM}/{Pages.BASKET}/'


class QueryParams:
    PROMO = 'promo'
