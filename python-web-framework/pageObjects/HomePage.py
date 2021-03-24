from selenium.webdriver.common.by import By
from pageObjects.CheckOutPage import CheckOutPage
import time


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop123']")
    name = (By.CSS_SELECTOR, ".form-group input[name='name']")
    email = (By.CSS_SELECTOR, ".form-group input[name='email']")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def clickShopLink(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
