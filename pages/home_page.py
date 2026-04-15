from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    products_list_element = (By.CSS_SELECTOR, ".product-image-wrapper")
    add_to_cart_button_element = (By.CSS_SELECTOR, ".add-to-cart")
    product_added_popup_element = (By.CSS_SELECTOR, ".modal-content")
    success_message_element = (By.XPATH, "//p[contains(. , 'Your product has been added to cart.')]")
    continue_shopping_btn_element = (By.CSS_SELECTOR, ".btn-block")
    all_products_list = (By.XPATH, "//div[@class ='product-image-wrapper']")
    product_name_element = (By.CSS_SELECTOR, ".productinfo p")
    add_to_cart_element = (By.CSS_SELECTOR, ".add-to-cart")


    def add_product_to_cart(self,item_name):
        products_list = self.get_elements(self.products_list_element)
        for product in products_list:
            raw_text = product.text
            product_name = " ".join(raw_text.split())
            if item_name.lower() in product_name.lower():
                add_to_cart_btn = product.find_element(*self.add_to_cart_button_element)
                self.js_click_element(add_to_cart_btn)
                break

    def click_continue_shopping_button(self):
        self.click(self.continue_shopping_btn_element)

    def is_added_product_popup_visible(self):
        return self.is_visible(self.product_added_popup_element)

    def get_popup_text(self):
        success_message = self.get_text(self.success_message_element)
        return success_message

    def get_all_product_names(self):
        product_names_list = []
        all_products = self.get_elements(   self.all_products_list)
        for product in all_products:
            product_name= product.find_element(*self.product_name_element).text
            product_names_list.append(product_name)
        return product_names_list