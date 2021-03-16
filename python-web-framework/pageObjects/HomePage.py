from selenium.webdriver.common.by import By
from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def clickShopLink(self):
        # driver.find_element_by_css_selector("a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()  # To deserialize the tuple add "*"
        return CheckOutPage(self.driver)
