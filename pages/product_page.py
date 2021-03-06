from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_product_link.click()
        self.solve_quiz_and_get_code()

    def should_be_add_message(self):
        message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
        product_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ADD_MESSAGE)
        product = self.browser.find_element(*ProductPageLocators.PRODUCT)
        assert product.text == product_in_message.text and "has been added to your basket." in message.text, \
            f"Add message is not present or incorrect. Message text = {message.text}, product text = {product.text}"

    def should_be_cart_message_with_correct_price(self):
        message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        assert price.text in message.text and "Your basket total is now" in message.text, \
            "Price message is not present or incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
