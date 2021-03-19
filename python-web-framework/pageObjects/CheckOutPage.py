from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, "a.btn-primary")
    # Trigger point to move to next page
    checkOutSuccess = (By.CSS_SELECTOR, "button.btn.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def clickAddMobile(self, title):
        card_titles = self.driver.find_elements(*CheckOutPage.cardTitle)
        print(type(card_titles))
        i = -1
        for card_title in card_titles:
            i += 1
            if card_title.text == title:
                self.driver.find_elements(*CheckOutPage.cardFooter)[i].click()
        self.driver.find_element(*CheckOutPage.checkOut).click()

    # Trigger point to switch to next page
    def clickCheckOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOutSuccess).click()
        return ConfirmPage(self.driver)
