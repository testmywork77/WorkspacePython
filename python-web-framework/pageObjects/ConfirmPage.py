import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ConfirmPage:
    countryTxt = (By.CSS_SELECTOR, "#country")
    termsAndConditionsChk = (By.CSS_SELECTOR, "div.checkbox.checkbox-primary")
    purchaseBtn = (By.CSS_SELECTOR, "input[value='Purchase']")

    def __init__(self, driver):
        self.driver = driver

    def enterDeliverLocation(self, text):
        self.driver.find_element(*ConfirmPage.countryTxt).send_keys(text)

    def selectDeliveryLocation(self, country_option):
        country_option.click()

    def clickTermsAndConditionsChk(self):
        time.sleep(3)
        self.driver.find_element(*ConfirmPage.termsAndConditionsChk).click()

    def clickPurchase(self):
        self.driver.find_element(*ConfirmPage.purchaseBtn).click()

    def checkPurchaseButtonExists(self):
        try:
            self.driver.find_element(*ConfirmPage.purchaseBtn)
        except NoSuchElementException:
            return False
        return True
