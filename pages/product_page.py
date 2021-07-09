from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(
                 *ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def check_product_added_basket(self):
        book = self.browser.find_element(
               *ProductPageLocators.BOOK)
        book_msg = self.browser.find_element(
                   *ProductPageLocators.BOOK_MSG)
        assert book.text == book_msg.text, \
               f"The book <{book.text}> added with name <{book_msg.text}>"
        cost = self.browser.find_element(
               *ProductPageLocators.COST)
        cost_msg = self.browser.find_element(
                   *ProductPageLocators.COST_MSG)
        assert cost.text == cost_msg.text, \
               f"The cost <{cost.text}> diffirent from basket <{cost_msg.text}>"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is not disappeared, but should was" 
