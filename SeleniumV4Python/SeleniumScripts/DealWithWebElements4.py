# By Class In Selenium with Python -How To Fix find_element_by_* commands are deprecated warning.
# By XPath, CssSelector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

# By XPath, CssSelector
username = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
login = driver.find_element(By.XPATH, "//input[@value='LOGIN']")
username.send_keys("Admin")
password.send_keys("admin123")
login.click()

time.sleep(2)
assert "dashboard" in driver.current_url
welcomeLnk = driver.find_element(By.XPATH, "//a[contains(text(),'Welcome')]")
welcomeLnk.click()
time.sleep(2)
logoutLnk = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
logoutLnk.click()
assert "login" in driver.current_url

time.sleep(5)
driver.quit()
