from selenium.webdriver.common.by import By


class CheckOutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")
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

    def clickCheckOut(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()

    def clickCheckOutSuccess(self):
        self.driver.find_element(*CheckOutPage.checkOutSuccess).click()
