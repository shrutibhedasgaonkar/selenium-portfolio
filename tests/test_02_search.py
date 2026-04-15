from pages.home_page import HomePage
from pages.login_page import Login_Page



class TestSearch:
    def test_add_to_cart(self, driver):
        driver.get("https://www.automationexercise.com/login")
        account_page = Login_Page(driver)
        account_page.login("srbsrp@gmail.com", "Qazqaz@123")

        driver.get("https://www.automationexercise.com/products")

        home_page = HomePage(driver)
        home_page.add_product_to_cart("Sleeveless Dress")

        assert home_page.is_added_product_popup_visible() == True, "Add to cart modal did not appear"
        assert "Your product has been added to cart." in home_page.get_popup_text(), f"Unexpected message: {home_page.get_popup_text()}"

        home_page.click_continue_shopping_button()

