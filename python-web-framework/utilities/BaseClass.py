import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(By.LINK_TEXT, text)
        )
