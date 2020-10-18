from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

'''Alert Pop Up'''
signIn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
signIn.click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # accept it, Click on OK
# alert.dismiss()  # Cancel the alert Pop Up

driver.switch_to.default_content()

time.sleep(3)
driver.quit()
