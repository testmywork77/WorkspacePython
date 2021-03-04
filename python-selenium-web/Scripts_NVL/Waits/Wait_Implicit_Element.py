from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
# time_out is 10 milli sec, dynamic wait, implicit wait applied only for web elements
# it's Global wait, applicable for find_element and find_elements
# implicit wait not for non-web elements: title, url, alerts
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://app.hubspot.com/login')
print(driver.title)

# HubSpot Login
# time.sleep(5)
# print(driver.title)

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("test@gmail.com")
driver.find_element(By.ID, 'password').send_keys("test1234")

driver.close()
