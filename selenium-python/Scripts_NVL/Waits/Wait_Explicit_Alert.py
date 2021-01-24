# Explicit Wait- alert_is_present
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()

wait = WebDriverWait(driver, 10)
proceed = wait.until(ec.element_to_be_clickable((By.NAME, 'proceed')))
proceed.click()

alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()

driver.close()
