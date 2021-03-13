from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

username = driver.find_element_by_id("txtUsername")
username.send_keys("Admin")
password = driver.find_element_by_name("txtPassword")
password.send_keys("admin123")
login = driver.find_element_by_class_name("button")
login.click()

time.sleep(5)
driver.quit()
