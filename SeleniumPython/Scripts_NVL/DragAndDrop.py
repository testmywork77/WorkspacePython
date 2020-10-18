from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')


'''drag and drop'''
draggableElement = driver.find_element(By.CSS_SELECTOR, '#draggable')
droppableElement = driver.find_element(By.CSS_SELECTOR, '#droppable')
action_chains = ActionChains(driver)

# Single step
# action_chains.drag_and_drop(draggableElement, droppableElement).perform()

# Multiple steps
action_chains\
    .click_and_hold(draggableElement)\
    .move_to_element(droppableElement)\
    .release()\
    .perform()

time.sleep(3)
driver.quit()
