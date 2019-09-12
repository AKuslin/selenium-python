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
    REG_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[text()='Add to basket']")
    BASKET_TOTAL = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_NAME_NOTIFICATION = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    PRODUCT_PRICE_NOTIFICATION = (By.XPATH, "(//div[@class='alertinner ']//strong)[3]")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_TEXT = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")