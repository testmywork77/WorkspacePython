from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# Industry, Form_submitForm_Industry
industryDropDown = driver.find_element(By.ID, "Form_submitForm_Industry")
selectIndustry = Select(industryDropDown)
# <option value="Education">Education</option>
selectIndustry.select_by_visible_text("Education")
# selectIndustry.select_by_value("Education")
# selectIndustry.select_by_index(8)

# Is DropDown is multi select or not
print(f"Is DropDown is multi select or not: {selectIndustry.is_multiple}")

# <option value="United Kingdom">United Kingdom</option>
# <option value="India">India</option>
# Form_submitForm_Country
countryDropDown = driver.find_element(By.ID, "Form_submitForm_Country")
selectCountry = Select(countryDropDown)
selectCountry.select_by_visible_text("India")

time.sleep(5)
driver.quit()
