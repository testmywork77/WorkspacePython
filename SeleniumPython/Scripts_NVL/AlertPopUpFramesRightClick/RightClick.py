from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
time.sleep(2)

'''right/context click'''
right_click_ele = driver.find_element(By.XPATH, "//span[text()='right click me']")
action_chains = ActionChains(driver)
action_chains.context_click(right_click_ele).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-icon span")
for right_click_option in right_click_options:
    print(right_click_option)
    if right_click_option.text == "Copy":
        right_click_option.click()
        break


time.sleep(3)
driver.quit()


