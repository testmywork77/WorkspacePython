from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
myPageTitle = driver.title
print(myPageTitle)
assert "OrangeHRM" in myPageTitle

username = driver.find_element_by_id("txtUsername")

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

password = driver.find_element_by_name("txtPassword")
password.send_keys("admin123")

login = driver.find_element_by_class_name("button")
login.click()

time.sleep(5)
driver.quit()
