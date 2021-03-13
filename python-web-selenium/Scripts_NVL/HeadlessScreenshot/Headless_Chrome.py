from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://app.hubspot.com/login')
time.sleep(5)
# HubSpot Login
print(driver.title)
