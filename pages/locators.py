from selenium.webdriver.common.by import By

#class MainPageLocators():

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK = (By.CSS_SELECTOR, 'div.product_main>h1')
    BOOK_MSG = (By.CSS_SELECTOR, 'div.alertinner>strong')
    COST = (By.CSS_SELECTOR, '.product_main>.price_color')
    COST_MSG = (By.CSS_SELECTOR, 'div.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')
