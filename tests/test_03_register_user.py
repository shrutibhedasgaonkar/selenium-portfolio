from pages.account_created import AccountCreatedSuccess
from pages.signup_page import UserRegister


class Test_Register:
    def test_valid_register_user(self, driver):
        user_data = {
            "Title": "Mrs",
            "name": "Testtuxxo",
            "email": "testoiuqxx@gmail.com",
            "password": "qwertrew112",
            "first_name": "Test01x",
            "last_name": "testlastnamex",
            "Address1": "Address1,street1",
            "Address2": "Address2, Street2",
            "State": "Maharashtra",
            "City": "Mumbai",
            "Zipcode": "411098",
            "Mobile_num":"09876735462"
        }

        driver.get("https://www.automationexercise.com/login")
        register_user = UserRegister(driver)
        register_user.signup_user(user_data["name"],user_data["email"])
        assert "ENTER ACCOUNT INFORMATION" in register_user.signup_register_page_title(), "Page is not signup page"

        register_user.fill_signup_form(user_data)

        account_create = AccountCreatedSuccess(driver)
        assert "ACCOUNT CREATED!" in account_create.success_account(), "This is not the account create page"

        account_create.click_continue_btn()

