from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://www.londonfreelance.org/courses/frames/index.html')

'''Frames'''
driver.switch_to.frame(2)
headerValue = driver.find_element(By.CSS_SELECTOR, 'h2').text
print(headerValue)

driver.switch_to.default_content()
# driver.switch_to.parent_frame()

time.sleep(3)
driver.quit()

