from pages.contact_us_page import ContactUsPage


class TestContactUs:
    def test_fill_contact_us_form(self, driver):
        contact_form = {
            "name" : "Test00xx",
            "email": "testooxtest@test.com",
            "subject": "Test Subject",
            "message": "This is to test the message in contact us page"
        }

        driver.get("https://automationexercise.com/contact_us")
        contact = ContactUsPage(driver)
        contact.fill_contact_form(contact_form)

        assert "Success! Your details have been submitted successfully." in contact.success_submit_message(),\
                                                                    "There is no success message after submission."

