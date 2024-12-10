import time

from selenium.webdriver.common.by import By

from base.base_page import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Base):
    # Locators
    product_name = "//a[@title='Сывороточный протеин VPLAB Vanilla 500 г']"
    delete_products = "//a[@title='Очистить корзину']"
    confirm_delete_products = "(//*[contains(text(), 'Очистить корзину')])[2]"


    # Getters
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_delete_products(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_products)))

    def get_confirm_delete_products(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_delete_products)))

    # Actions
    def save_product_name(self):
        return self.get_product_name().text

    def click_delete_products(self):
        self.move_to(self.get_delete_products())
        self.get_delete_products().click()

    def click_confirm_delete_products(self):
        self.move_to(self.get_confirm_delete_products())
        self.get_confirm_delete_products().click()

    # Methods
    def finish(self):
        assert self.save_product_name() == 'Сывороточный протеин VPLAB Vanilla 500 г'
        self.get_screenshot()
        time.sleep(5)
        self.click_delete_products()
        self.click_confirm_delete_products()
