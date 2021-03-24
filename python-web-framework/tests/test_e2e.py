import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import *


class TestE2E(BaseClass):
    # @pytest.mark.skip
    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        check_out_page = home_page.clickShopLink()  # To get Shop items
        log.info("Getting all the card titles")
        # CheckOut Page
        check_out_page.clickAddMobile("Blackberry")
        confirm_page = check_out_page.clickCheckOutItems()  # Final checkOut Items
        # Confirm Page
        log.info("Enter country as ind")
        confirm_page.enterDeliverLocation("ind")
        country_option = self.verifyLinkPresence("India")
        if country_option is not None:
            confirm_page.selectDeliveryLocation(country_option)
            confirm_page.clickTermsAndConditionsChk()
            confirm_page.clickPurchase()
        assert 1 == 3
        # assert confirm_page.checkPurchaseButtonExists()
        # self.verifyLinkPresence("India")
