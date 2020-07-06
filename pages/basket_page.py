from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert "Your basket is empty." in basket_empty.text, f"Basket is not empty. Basket text = {basket_empty.text}"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_FORM), \
            "Products is presented, but should not be"