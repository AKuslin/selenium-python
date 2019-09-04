from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form1")
    REG_FORM = (By.ID, "register_form1")
    EMAIL_LOGIN = (By.NAME, "login-username")
    PASSWORD_LOGIN = (By.NAME, "login-password")
    EMAIL_REG = (By.NAME, "registration-email")
    PASSWORD1_REG = (By.NAME, "registration-password1")
    PASSWORD2_REG = (By.NAME, "registration-password2")