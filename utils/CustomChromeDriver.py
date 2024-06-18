from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def customChrome():
    option= Options()
    option.add_argument("--enable-extentions")

    drivers=webdriver.Chrome(chrome_options=option, executable_path="../drivers/chromedriver.exe")
    drivers.implicitly_wait(3)
    drivers.maximize_window()

    print("[Open browser]")
    return drivers
