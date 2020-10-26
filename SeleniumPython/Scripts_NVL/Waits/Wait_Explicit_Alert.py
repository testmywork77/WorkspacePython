# Explicit Wait- alert_is_present
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()

driver.find_element(By.NAME, 'proceed').click()

wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()

driver.close()



