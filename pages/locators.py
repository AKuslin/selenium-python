from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    EMAIL_LOGIN = (By.NAME, "login-username")
    PASSWORD_LOGIN = (By.NAME, "login-password")
    EMAIL_REG = (By.NAME, "registration-email")
    PASSWORD1_REG = (By.NAME, "registration-password1")
    PASSWORD2_REG = (By.NAME, "registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[text()='Add to basket']")
    BASKET_TOTAL = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")