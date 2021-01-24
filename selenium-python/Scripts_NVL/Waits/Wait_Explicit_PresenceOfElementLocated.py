# Explicit Wait- title_is, presence_of_element_located
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get('https://app.hubspot.com/login')
driver.maximize_window()

wait.until(ec.title_is('HubSpot Login'))  # HubSpot Login
print(driver.title)
# Element available inside the DOM, but may or may not be on Page
# To whether element is on Page,
user_name = wait.until(ec.presence_of_element_located((By.ID, 'username')))
user_name.send_keys("test@gmail.com")
driver.find_element(By.ID, 'password').send_keys("test1234")

driver.close()
