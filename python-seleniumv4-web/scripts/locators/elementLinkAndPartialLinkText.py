# By Class In Selenium with Python -How To Fix find_element_by_* commands are deprecated warning.
# By LinkText, PartialLinkText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)
assert "OrangeHRM" in driver.title


# By LinkText, PartialLinkText
# forgotLnk = driver.find_element(By.LINK_TEXT, "Forgot your password?")
# By PartialLinkText
forgotLnk = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot your")

forgotLnk.click()

time.sleep(2)
assert "requestPasswordResetCode" in driver.current_url
driver.quit()
