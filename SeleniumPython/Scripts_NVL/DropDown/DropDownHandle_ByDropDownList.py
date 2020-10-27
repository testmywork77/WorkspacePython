from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


def select_option_from_optionList(options, text):
    for option in options:
        print(option.text)
        if option.text == text:
            option.click()
            break


def select_option_from_dropdown(dropdown, text):
    select = Select(dropdown)
    options = select.options
    for option in options:
        print(option.text)
        if option.text == text:
            option.click()
            break


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# Industry, Form_submitForm_Industry
industryDropDown = driver.find_element(By.ID, "Form_submitForm_Industry")
countryDropDown = driver.find_element(By.ID, "Form_submitForm_Country")
# With Select
select_option_from_dropdown(industryDropDown, "Healthcare")
select_option_from_dropdown(countryDropDown, "United Kingdom")

# Without Select - Get Options directly
industry_options = driver.find_elements(By.CSS_SELECTOR, "select#Form_submitForm_Industry > option")
country_options = driver.find_elements(By.CSS_SELECTOR, "select#Form_submitForm_Country > option")
select_option_from_optionList(industry_options, "Education")
select_option_from_optionList(country_options, "India")

time.sleep(10)
driver.quit()
