from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


def select_option_by_text(element, text):
    select = Select(element)
    select.select_by_visible_text(text)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

industryDropDown = driver.find_element(By.ID, "Form_submitForm_Industry")
countryDropDown = driver.find_element(By.ID, "Form_submitForm_Country")

select_option_by_text(industryDropDown, "Education")
select_option_by_text(countryDropDown, "India")

time.sleep(5)
driver.quit()
