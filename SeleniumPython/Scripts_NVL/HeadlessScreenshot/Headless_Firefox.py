from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

options = webdriver.FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://app.hubspot.com/login')
time.sleep(5)
# HubSpot Login
print(driver.title)
