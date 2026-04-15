from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserRegister(BasePage):
    signup_name_element = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    signup_email_element = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signup_btn_element = (By.XPATH, "//button[@data-qa='signup-button']")
    signup_error_msg_element = (By.XPATH, "//p[contains(., 'Email Address already exist!')]")
    signup_register_form_title_element = (By.CSS_SELECTOR, ".title")

    signup_Mr_radio_btn = (By.XPATH, "//input[@value = 'Mr']")
    signup_Mrs_radio_btn = (By.XPATH, "//input[@value = 'Mrs']")
    #signup_form_name_element = (By.XPATH, "//input[@data-qa='name']")
    #signup_form_email_element = (By.XPATH, "//input[@data-qa='email']")
    signup_form_password_element = (By.XPATH, "//   input[@data-qa='password']")
    signup_form_day_dropdown_element = (By.XPATH, "//select[@data-qa='days']")
    signup_form_month_dropdown_element = (By.XPATH, "//select[@data-qa='months']")
    signup_form_year_dropdown_element = (By.XPATH, "//select[@data-qa='years']")
    signup_form_first_name_element = (By.XPATH, "//input[@data-qa='first_name']")
    signup_form_last_name_element = (By.XPATH, "//input[@data-qa='last_name']")
    signup_form_address1_element = (By.XPATH, "//input[@data-qa='address']")
    signup_form_address2_element = (By.XPATH, "//input[@data-qa='address2']")
    signup_form_state_element = (By.XPATH, "//input[@data-qa='state']")
    signup_form_city_element = (By.XPATH, "//input[@data-qa='city']")
    signup_form_zipcode_element = (By.XPATH, "//input[@data-qa='zipcode']")
    signup_form_mobile_num_element = (By.XPATH, "//input[@data-qa='mobile_number']")
    signup_form_submit_btn_element = (By.XPATH, "//button[@data-qa='create-account']")


    def signup_user(self, name, email_id):
        self.type_text(self.signup_name_element, name)
        self.type_text(self.signup_email_element, email_id)
        self.click(self.signup_btn_element)

    def already_email_error(self):
        return self.get_text(self.signup_error_msg_element)

    def signup_register_page_title(self):
        title_text = self.get_text(self.signup_register_form_title_element)
        return title_text

    def fill_signup_form(self, user_data):
        #self.type_text(self.signup_name_element, user_data["name"])
        #self.type_text(self.signup_email_element, user_data["email"])
        self.type_text(self.signup_form_password_element, user_data["password"])
        self.select_dropdown_value(self.signup_form_day_dropdown_element, 5)
        self.select_dropdown_value(self.signup_form_month_dropdown_element, 6)
        self.select_dropdown_value(self.signup_form_year_dropdown_element, 1990)
        if user_data["Title"] == "Mr":
            self.click_radio(self.signup_Mr_radio_btn)
        elif user_data["Title"] == "Mrs":
            self.click_radio(self.signup_Mrs_radio_btn)

        self.type_text(self.signup_form_first_name_element, user_data["first_name"])
        self.type_text(self.signup_form_last_name_element, user_data["last_name"])
        self.type_text(self.signup_form_address1_element, user_data["Address1"])
        self.type_text(self.signup_form_address2_element, user_data["Address2"])
        self.type_text(self.signup_form_state_element, user_data["State"])
        self.type_text(self.signup_form_city_element, user_data["City"])
        self.type_text(self.signup_form_zipcode_element, user_data["Zipcode"])
        self.type_text(self.signup_form_mobile_num_element, user_data["Mobile_num"])

        self.click(self.signup_form_submit_btn_element)
