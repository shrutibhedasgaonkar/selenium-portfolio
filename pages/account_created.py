from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountCreatedSuccess(BasePage):
    success_message_text = (By.XPATH, "//h2[@data-qa = 'account-created']")
    continue_btn_element = (By.CSS_SELECTOR, "a[data-qa = 'continue-button']")

    def success_account(self):
        success_msg = self.get_text(self.success_message_text)
        return success_msg

    def click_continue_btn(self):
        self.click(self.continue_btn_element)
