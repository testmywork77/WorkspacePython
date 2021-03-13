from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)

driver.find_element(By.CSS_SELECTOR, "button[onclick='myFunction()']").click()
time.sleep(5)

driver.switch_to.alert.accept()  # closes alert window using OK button
driver.switch_to.alert.dismiss()  # closes alert window using cancel button


driver.quit()

