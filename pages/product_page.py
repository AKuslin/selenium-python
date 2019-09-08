from .base_page import BasePage
from .locators import ProductPageLocators
#from selenium.common.exceptions import NoAlertPresentException
#import math

class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    # def should_be_product_page(self):
    #     self.should_be_add_to_basket()
    #     self.should_be_product_page_url()
    #
    # def should_be_add_to_basket(self):
    #     assert BasePage.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "'add to basket' button is not presented"
    #
    # def should_be_product_page_url(self):
    #     assert self.browser.current_url() == "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear", "Wrong URL"
    #
    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")