import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


# Common methods for all the tests/pages
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        # file_handler = logging.FileHandler('../logs/logfile.log')
        file_handler = logging.FileHandler('./logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # file_handler object
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        return logger

    def verifyLinkPresence(self, text):
        try:
            country_link = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.LINK_TEXT, text)))
            return country_link
        except NoSuchElementException:
            return None

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
