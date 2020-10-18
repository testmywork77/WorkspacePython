from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://app.hubspot.com/login')

time.sleep(5)
'''Send Keys and Click using ActionChains'''
username_ele = driver.find_element(By.ID, 'username')
password_ele = driver.find_element(By.ID, 'password')
login_button_ele = driver.find_element(By.ID, 'loginBtn')

action_chains = ActionChains(driver)
action_chains.send_keys_to_element(username_ele, 'myname@gmail.com')
action_chains.send_keys_to_element(password_ele, 'mypassword')
# action_chains.click(login_button_ele).perform()

time.sleep(3)
driver.quit()


