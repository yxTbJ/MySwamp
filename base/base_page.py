from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        file_name = '.\\screenshots\\screenshot' + str(now_date) + '.png'
        self.driver.get_screenshot_as_file(file_name)

    def move_to(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()



