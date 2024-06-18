from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VerifyLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        return self.driver.title