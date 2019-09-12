from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket emty text is not present"

    def should_be_item_is_not_present_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "basket item is presented, but should not be"