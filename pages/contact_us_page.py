from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactUsPage(BasePage):
    name_input_element = (By.XPATH, "//input[@data-qa = 'name']")
    email_input_element = (By.XPATH, "//input[@data-qa = 'email']")
    subject_input_element = (By.XPATH, "//input[@data-qa = 'subject']")
    message_input_element = (By.XPATH, "//textarea[@data-qa = 'message']")
    submit_button_element = (By.XPATH, "//input[@data-qa = 'submit-button']")
    submit_success_msg_element = (By.XPATH, "//div[@class = 'status alert alert-success']")

    def fill_contact_form(self, contact_form):
        self.type_text(self.name_input_element, contact_form["name"])
        self.type_text(self.email_input_element, contact_form["email"])
        self.type_text(self.subject_input_element, contact_form["subject"])
        self.type_text(self.message_input_element, contact_form["message"])

        self.click(self.submit_button_element)

        self.click_alert_popups()

    def success_submit_message(self):
        return self.get_text(self.submit_success_msg_element)
