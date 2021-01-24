from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.co.uk/")

linksList = driver.find_elements(By.TAG_NAME, 'a')
print(f"Links count: {len(linksList)}")
for link in linksList:
    print(link.text)
    print(link.get_attribute('href'))

imagesList = driver.find_elements(By.TAG_NAME, 'img')
print(f"Images count: {len(imagesList)}")
for image in imagesList:
    print(image.get_attribute('src'))

time.sleep(5)
driver.quit()
