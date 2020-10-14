from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)

time.sleep(5)
# By finding all the web elements using iframe tag
iframeElements = driver.find_elements(By.TAG_NAME, "iframe")
print(f"Frames count: {len(iframeElements)}")

# Switching Frames in Selenium using Index
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, 'div#introAgreeButton').click()

driver.find_element(By.NAME, 'q').send_keys("naveen automation labs")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == "naveen automation labs blog":
        ele.click
        break

time.sleep(5)
driver.quit()

