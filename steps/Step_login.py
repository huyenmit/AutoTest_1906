from selenium.webdriver.common.by import By
from pages.Page_login import page_login


class stepLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.inputUserName(username)
        self.inputPassword(password)
        self.clickButton()

    # Action
    def inputUserName(self, email):
        self.get_txtUsername().send_keys(email)

    def inputPassword(self, password):
        self.get_txtpassword().send_keys(password)

    def clickButton(self):
        self.get_btnLogin().click()

    # Get element
    def get_txtUsername(self):
        return self.driver.find_element(By.XPATH, page_login().txt_username())

    def get_txtpassword(self):
        return self.driver.find_element(By.XPATH, page_login().txt_password())

    def get_btnLogin(self):
        return self.driver.find_element(By.XPATH, page_login().bt_login())
