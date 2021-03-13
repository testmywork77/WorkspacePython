from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://app.hubspot.com/login")

form = driver.find_element(By.ID, 'hs-login')
driver.execute_script("arguments[0].style.border = '3px solid red'", form)
time.sleep(3)
driver.close()
