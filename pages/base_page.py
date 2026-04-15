from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Waits for element, clears it, types text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Waits for element then returns its text."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_visible(self, locator):
        """Returns True if element is visible, False if not."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_title(self):
        """Returns current page title."""
        return self.driver.title

    def select_dropdown_value(self, locator, value):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        Select(element).select_by_value(str(value))

    def click_radio(self, locator):
        radio = self.wait.until(EC.element_to_be_clickable(locator))
        radio.click()

    def click_alert_popups(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
        except:
            pass


    def handle_consent_popup(self):
        """Handles consent popup if it appears."""
        try:
            consent_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//p[@class='fc-button-label' and text()='Consent']")
                )
            )
            consent_button.click()
        except:
            pass

    def js_click(self, locator):
        """
        JavaScript click using a locator.Used when an overlay blocks a standard click.
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def js_click_element(self, element):
        """
        JavaScript click on an already-found WebElement.
        Used when element was found via find_element on a parent WebElement.
        """
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        """Scrolls page until element is in viewport."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def wait_for_url_to_contain(self,url_part):
        return self.wait.until(EC.url_contains(url_part))


