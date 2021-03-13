from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

'''File Upload Pop Up'''
'''This will work if the element have type as "file" <input type="file" name="upfile">'''
file = driver.find_element(By.CSS_SELECTOR, 'input[type=file]')
file.send_keys('C:\\PythonExamples\\python_testfile.txt')

submit = driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
submit.click()

time.sleep(3)
driver.quit()
