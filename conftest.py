import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver

from pages.base_page import BasePage

base_url = "https://www.automationexercise.com"

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    browser.get(base_url)
    BasePage(browser).handle_consent_popup()

    yield browser
