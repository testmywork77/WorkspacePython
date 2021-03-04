from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.spicejet.com/')
time.sleep(3)

'''Move To Element'''
login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
act_chains = ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

time.sleep(2)
spice_club_members_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
act_chains.move_to_element(spice_club_members_ele).perform()

time.sleep(2)
member_login_ele = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login_ele.click()

time.sleep(3)
driver.quit()
