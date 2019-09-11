from .base_page import BasePage
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Wrong URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self):
        self.go_to_login_page()
        f = faker.Faker()
        email = f.email()
        password = f.password()
        print("email: " + email)
        print("pass: " + password)
        login = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        login.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_REG)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_REG)
        password2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()