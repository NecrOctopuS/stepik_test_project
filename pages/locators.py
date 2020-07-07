from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADD_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner')
    PRODUCT_IN_ADD_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, ".price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success div.alertinner")


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_PRODUCT_FORM = (By.CSS_SELECTOR, "#basket_formset")
