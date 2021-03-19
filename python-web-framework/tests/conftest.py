import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:/WebDrivers/geckodriver.exe')
        print("Launching firefox browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path='C:/WebDrivers/msedgedriver.exe')
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
        print("Launching chrome browser.........")
    # driver.get("http://admin-demo.nopcommerce.com")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):  # This will get the value from Command Line
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


'''
# ########## pytest HTML Report ################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Tester'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
'''
