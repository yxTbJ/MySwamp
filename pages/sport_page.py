import time

from selenium.webdriver.common.by import By

from base.base_page import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sport_page(Base):
    # Locators
    sports_nutrition_category = "//a[@title='Спортивное питание']"

    # Getters
    def get_sports_nutrition_category_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sports_nutrition_category)))

    # Actions
    def click_sports_nutrition_category_button(self):
        self.move_to(self.get_sports_nutrition_category_button())
        self.get_sports_nutrition_category_button().click()

    # Methods