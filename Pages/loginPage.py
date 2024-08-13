from selenium.webdriver.common.by import By

from BasePage.basePage import BasePage


class LoginPage(BasePage):
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test='error']")
    blank_username = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.enter_text(self.username_field, username)

    def enter_password(self, password):
        self.enter_text(self.password_field, password)

    def error_displayed(self):
        return self.wait_for_element(self.error_message)
        # self.wait_for_element(self.ERROR_MESSAGE)

    def click_login(self):
        self.click_element(self.login_button)

    def get_username_placeholder(self):
        return self.get_attribute_value(self.username_field, "placeholder")

    def get_password_placeholder(self):
        return self.get_attribute_value(self.password_field, "placeholder")



