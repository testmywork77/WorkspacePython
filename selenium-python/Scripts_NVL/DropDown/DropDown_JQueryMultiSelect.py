from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


def select_values(options, values):
    if not values[0] == 'all':
        for option in options:
            print(option.text)
            for value in values:
                if option.text == value:
                    option.click()
                    break
    else:
        try:
            for option in options:
                option.click()
        except Exception as e:
            print(e)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)
option_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
# select_values_list = ['choice 2', 'choice 4', 'choice 6 1', 'choice 6 2 1']
# select_values_list = ['choice 3']
select_values_list = ['all']
select_values(option_list, select_values_list)

time.sleep(5)
driver.quit()
