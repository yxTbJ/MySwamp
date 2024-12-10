import time

from selenium.webdriver.common.by import By

from base.base_page import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sportpit_page(Base):
    # Locators
    protein_category = "//a[@title='Протеины']"

    # Getters
    def get_protein_category_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.protein_category)))

    # Actions
    def click_protein_category_button(self):
        self.move_to(self.get_protein_category_button())
        self.get_protein_category_button().click()

    # Methods