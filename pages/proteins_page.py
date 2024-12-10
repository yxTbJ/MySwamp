import time

from selenium.webdriver.common.by import By

from base.base_page import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Proteins_page(Base):
    # Locators
    filter_brand_vp = "//a[@title='VP LABORATORY']"
    filter_whey = "(// *[contains(text(), 'сывороточный')])[2]"
    filter_vanilla = "(// *[contains(text(), 'ваниль')])[2]"
    display_filtered = "//a[@title='Показать товары по выбранным условиям']"
    add_to_cart = "//a[@title='Купить Сывороточный протеин VPLAB Vanilla 500 г']"
    place_an_order = "//a[@title='Оформить заказ']"

    # Getters
    def get_filter_brand_vp_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_vp)))

    def get_filter_whey_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_whey)))

    def get_filter_vanilla_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_vanilla)))

    def get_display_filtered_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.display_filtered)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_place_an_order_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.place_an_order)))

    # Actions
    def click_filter_brand_vp_button(self):
        self.move_to(self.get_filter_brand_vp_button())
        self.get_filter_brand_vp_button().click()

    def click_filter_whey_button(self):
        self.move_to(self.get_filter_whey_button())
        self.get_filter_whey_button().click()

    def click_filter_vanilla_button(self):
        self.move_to(self.get_filter_vanilla_button())
        self.get_filter_vanilla_button().click()

    def click_display_filtered_button(self):
        self.move_to(self.get_display_filtered_button())
        self.get_display_filtered_button().click()

    def click_add_to_cart_button(self):
        self.move_to(self.get_add_to_cart_button())
        self.get_add_to_cart_button().click()

    def click_place_an_order_button(self):
        self.move_to(self.get_place_an_order_button())
        self.get_place_an_order_button().click()

    # Methods

    def setting_up_filters(self):
        self.click_filter_brand_vp_button()
        self.click_filter_whey_button()
        self.click_filter_vanilla_button()
        time.sleep(10)
        self.click_display_filtered_button()

    def add_product_and_move_to_cart(self):
        self.click_add_to_cart_button()
        self.click_place_an_order_button()
