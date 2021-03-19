from utilities.BaseClass import BaseClass
from pageObjects.HomePage import *


class TestE2E(BaseClass):
    """
    def test_homePageTitle(self):
        act_title = self.driver.title

        if act_title == "ProtoCommerce":  # ProtoCommerce / Your store. Login
            # self.logger.info("**** Home page title test passed ****")
            # self.driver.close()
            assert True
        else:
            # self.logger.error("**** Home page title test failed ****")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            # self.driver.close()
            assert False
    """
    def test_e2e(self):
        # Home Page
        home_page = HomePage(self.driver)
        check_out_page = home_page.clickShopLink()  # To get Shop items
        # CheckOut Page
        check_out_page.clickAddMobile("Blackberry")
        confirm_page = check_out_page.clickCheckOutItems()  # Final checkOut Items
        # Confirm Page
        confirm_page.enterDeliverLocation()
        confirm_page.clickTermsAndConditionsChk()
        confirm_page.clickPurchase()
        # assert confirm_page.checkPurchaseButtonExists()
        # self.verifyLinkPresence("India")
