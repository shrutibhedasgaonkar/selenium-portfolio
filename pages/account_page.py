from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):

    logged_in_text = (By.XPATH, "//a[contains(., 'Logged in as')]")
    logged_in_username = (By.XPATH, "//ul/li/a/b")
    logout_button = (By.XPATH,"//a[@href= '/logout']")

    def is_logged_in(self):
        return self.is_visible(self.logged_in_text)

    def get_logged_in_username(self):
        return self.get_text(self.logged_in_username)




