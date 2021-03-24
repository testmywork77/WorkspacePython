from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
import pytest


# Form submission data feed by List of Dict/Tuple
class TestHomePage(BaseClass):

    # Data feed using List of tuples. Each tuple treated as single data set
    @pytest.mark.skip
    def test_FormSubmission_WithTupleData(self, get_tuple_data):
        self.formSubmission(get_tuple_data)

    # Data feed using List of dicts. Each dict treated as single data set
    @pytest.mark.skip
    def test_FormSubmission_WithDictData(self, get_dict_data):
        self.formSubmission(get_dict_data)

    # Data feed using List of dicts from external file.
    @pytest.mark.skip
    def test_FormSubmission_WithDictData_External(self, get_dict_data_external):
        self.formSubmission(get_dict_data_external)

    def formSubmission(self, data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        if type(data) is dict:
            log.info("Dictionary")
            log.info("Dict Name is " + data["Name"])
            homepage.getName().send_keys(data["Name"])
            homepage.getEmail().send_keys(data["Email"])
            self.selectOptionByText(homepage.getGender(), data["Gender"])
        else:
            log.info("Tuple")
            log.info("Tuple Gender is " + data[2])
            homepage.getName().send_keys(data[0])
            homepage.getEmail().send_keys(data[1])
            self.selectOptionByText(homepage.getGender(), data[2])
        homepage.getCheckBox().click()
        homepage.submitForm().click()
        alert_text = homepage.getSuccessMessage().text
        assert ("Success" in alert_text)
        self.driver.refresh()

    # pytest parameterization using tuples and access by index
    # Each tuple will treated as Dataset with in the List type as parameter
    @pytest.fixture(params=[("Name1", "Name1@gmail.com", "Male"), ("Name2", "Name2@gmail.com", "Female")])
    def get_tuple_data(self, request):
        return request.param

    # pytest parameterization using dicts and access by key
    # Each dict will treated as Dataset with in the List type as parameter
    @pytest.fixture(params=[{"Name": "Name1", "Email": "Name1@gmail.com", "Gender": "Male"},
                            {"Name": "Name2", "Email": "Name2@gmail.com", "Gender": "Female"}])
    def get_dict_data(self, request):
        return request.param

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def get_dict_data_external(self, request):
        return request.param
