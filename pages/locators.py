from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK = (By.CSS_SELECTOR, 'div.product_main>h1')
    BOOK_MSG = (By.CSS_SELECTOR, 'div.alertinner>strong')
    COST = (By.CSS_SELECTOR, '.product_main>.price_color')
    COST_MSG = (By.CSS_SELECTOR, 'div.alertinner>p>strong')
