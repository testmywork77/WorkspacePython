from utilities.BaseClass import BaseClass
from pageObjects.HomePage import *


class TestE2E(BaseClass):
    def test_homePageTitle(self):
        act_title = self.driver.title

        if act_title == "ProtoCommerce":    # ProtoCommerce / Your store. Login
            # self.logger.info("**** Home page title test passed ****")
            # self.driver.close()
            assert True
        else:
            # self.logger.error("**** Home page title test failed ****")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            # self.driver.close()
            assert False

    def test_e2e(self):
        home_page = HomePage(self.driver)
        check_out_page = home_page.clickShopLink()
        check_out_page.clickAddMobile("Blackberry")
        check_out_page.clickCheckOut()
        check_out_page.clickCheckOutSuccess()