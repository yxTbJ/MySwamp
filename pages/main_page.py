import time

from selenium.webdriver.common.by import By

from base.base_page import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):
    login = "testtesttest009@yandex.ru"
    password = "qwerty123/Y"

    # Locators
    move_to_autorization_popup_button = "//a[@title='Вход в Личный кабинет']"
    input_login = "//input[@name='login']"
    input_password = "//input[@name='password']"
    login_button = "//input[@name='submit']"
    catalog_button = "(//a[@title='Каталог товаров'])[1]"
    sport_button = "//*[contains(text(),'Спорт, отдых, туризм')]"

    # Getters
    def get_move_to_login_popup_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.move_to_autorization_popup_button)))

    def get_input_login(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.input_login)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_sport_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sport_button)))

    # Actions
    def click_move_to_login_popup_button(self):
        self.move_to(self.get_move_to_login_popup_button())
        self.get_move_to_login_popup_button().click()

    def input_login_value(self):
        self.get_input_login().send_keys(self.login)

    def input_password_value(self):
        self.get_input_password().send_keys(self.password)

    def click_login_button(self):
        self.move_to(self.get_login_button())
        self.get_login_button().click()

    def click_catalog_button(self):
        self.move_to(self.get_catalog_button())
        self.get_catalog_button().click()

    def click_sport_button(self):
        self.move_to(self.get_sport_button())
        self.get_sport_button().click()


    # Methods
    def autorization(self):
        self.click_move_to_login_popup_button()
        self.input_login_value()
        self.input_password_value()
        self.click_login_button()

    def pick_sport_category(self):
        self.click_catalog_button()
        self.click_sport_button()
