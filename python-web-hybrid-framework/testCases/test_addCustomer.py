import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class TestAddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************* TestAddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addCustomerPage = AddCustomerPage(self.driver)
        self.addCustomerPage.clickOnCustomersMenu()
        self.addCustomerPage.clickOnCustomersMenuItem()

        self.addCustomerPage.clickOnAddNew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addCustomerPage.setEmail(self.email)
        self.addCustomerPage.setPassword("test123")
        self.addCustomerPage.setFirstName("FName1")
        self.addCustomerPage.setLastName("LName1")
        self.addCustomerPage.setGender("Male")
        self.addCustomerPage.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addCustomerPage.setCompanyName("busyQA")
        self.addCustomerPage.setCustomerRoles("Guests")
        self.addCustomerPage.setManagerOfVendor("Vendor 2")
        self.addCustomerPage.setAdminContent("This is for testing.........")
        self.addCustomerPage.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
