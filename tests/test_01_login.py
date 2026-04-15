from pages.login_page import Login_Page


class TestLogin:
    def test_valid_login(self, driver):
        driver.get("https://www.automationexercise.com/login")

        login_page = Login_Page(driver)
        account_page = login_page.login("srbsrp@gmail.com", "Qazqaz@123")

        print(f"\nPage title after login: {driver.title}")
        print(f"\nCurrent URL after login: {driver.current_url}")

        assert account_page.is_logged_in() == True
        assert account_page.get_logged_in_username() == "test_selenium_srp"

    def test_invalid_login(self, driver):
        driver.get("https://www.automationexercise.com/login")
        login_page = Login_Page(driver)
        login_page.login("notregistered@example.com","somepassword123")

        assert login_page.is_error_message_visible() == True,  "Error message not displayed after invalid login"
        assert login_page.is_error_message_visible(), "Error message not displayed for unregistered email"
        assert "Your email or password is incorrect!" in login_page.get_error_message(), f"Unexpected error message: {login_page.get_error_message()}"




