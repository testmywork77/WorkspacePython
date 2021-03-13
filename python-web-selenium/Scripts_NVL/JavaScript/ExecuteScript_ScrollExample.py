# JavaScript Execute Script's Scroll- Top to Bottom and Bottom to Top
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://classic.crmpro.com/")

# Scroll Top to Bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)

# Scroll Bottom to Top of page
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
time.sleep(3)
driver.close()
