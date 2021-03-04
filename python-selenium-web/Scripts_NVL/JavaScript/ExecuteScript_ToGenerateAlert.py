from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://amazon.in")

wait = WebDriverWait(driver, 10)
# Generate Alert with JS execute-script method
driver.execute_script("alert('Hello World');")
alert = wait.until(ec.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
driver.switch_to.default_content()

time.sleep(3)
driver.close()
