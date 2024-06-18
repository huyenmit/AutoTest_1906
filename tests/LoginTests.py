import csv
import time
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import VerifyLogin
from HtmlTestRunner import HTMLTestRunner


class MyTestCase(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_argument("start-maximized")
        self.drivers = webdriver.Chrome()
        self.drivers.implicitly_wait(3)
        self.drivers.maximize_window()

        links = readDatatest.getLink('../linkFile.csv')
        for item in links:
            if item[0] == 'Login':
                self._dataTestAll = readDatatest.dataTestLogin(item[1])
                self._dataTest = self._dataTestAll[0]

    def tearDown(self):
        self.drivers.quit()

    def test_login(self):
        self.drivers.get(self._dataTest[2])
        stepLogin(self.drivers).login(self._dataTest[0], self._dataTest[1])
        time.sleep(5)
        self.expect = VerifyLogin(self.drivers).login()
        print(self.expect)
        self.assertIn(self._dataTest[3], self.expect, "Login fail")


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="../reports"))
