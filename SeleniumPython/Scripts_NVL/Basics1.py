from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)

time.sleep(5)
driver.switch_to_alert()  # switch to new window
driver.find_element(By.CSS_SELECTOR, 'div#introAgreeButton').click()
driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")

optionList = driver.find_element(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionList))

for option in optionList:
    print(option.text)
    if option.text == "naveen automationlabs youtube":
        option.click
        break

time.sleep(5)
driver.quit()

