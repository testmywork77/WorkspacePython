# By Class In Selenium with Python -How To Fix find_element_by_* commands are deprecated warning.
# By Id, Name, Class Name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

# By Id, Name, Class Name
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.NAME, "txtPassword")
login = driver.find_element(By.CLASS_NAME, "button")
username.send_keys("Admin")
password.send_keys("admin123")
login.click()
time.sleep(2)
assert "dashboard" in driver.current_url
driver.quit()
