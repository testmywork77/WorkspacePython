from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
myPageTitle = driver.title
print(myPageTitle)
assert "OrangeHRM" in myPageTitle

# Locators
USER_NAME = (By.ID, 'txtUsername')
PASSWORD = (By.NAME, 'txtPassword')
LOGIN = (By.CLASS_NAME, 'button')

# Web Elements -driver.find_element_by_* deprecated.
username = driver.find_element(By.ID, 'txtUsername')
password = driver.find_element(*PASSWORD)
login = driver.find_element(*LOGIN)

# WebElement methods
enableStatus = username.is_enabled()  # is enabled or not
isDisplayed = username.is_displayed()  # is displayed on the UI or not
print(f"enableStatus: {enableStatus}")
print(f"isDisplayed: {isDisplayed}")

username.clear()  # clear element's text

attrData = username.get_attribute("type")  # get attribute value
print(f"attrData: {attrData}")

fontValue = username.value_of_css_property("font-size")
print(f"font-size: {fontValue}")

username.send_keys("Admin")
password.send_keys("admin123")
login.click()

time.sleep(5)
assert "dashboard" in driver.current_url
driver.quit()
