from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_register_form()
        reg_email = self.browser.find_element(
                    *LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_pass1 = self.browser.find_element(
                    *LoginPageLocators.REG_PASS1)
        reg_pass1.send_keys(password)
        reg_pass2 = self.browser.find_element(
                    *LoginPageLocators.REG_PASS2)
        reg_pass2.send_keys(password)
        reg_button = self.browser.find_element(
                     *LoginPageLocators.REG_BUTTON)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Login url is not corrected"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
