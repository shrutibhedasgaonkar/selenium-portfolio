from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage


class Login_Page(BasePage):
    email_input = (By.CSS_SELECTOR, "[data-qa='login-email']")
    password_input = (By.CSS_SELECTOR, "[data-qa='login-password']")
    login_button = (By.CSS_SELECTOR, "[data-qa='login-button']")
    error_message = (By.CSS_SELECTOR, "[action='/login'] p")

    def login(self, email, password):
        self.type_text(self.email_input, email)
        self.type_text(self.password_input, password)
        self.click(self.login_button)
        return AccountPage(self.driver)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_error_message_visible(self):
        return self.is_visible(self.error_message)

