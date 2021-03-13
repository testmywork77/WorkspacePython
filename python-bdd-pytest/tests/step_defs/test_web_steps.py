import pytest

from pytest_bdd import scenario, scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Scenarios
# scenarios('../features/web.feature')
@scenario('../features/web.feature', 'Basic Search')
def test_search():
    pass


"""
# Moved the below fixture and Given step to conftest.py

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps
@given('the home page is displayed', target_fixture='ddg_home')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)
"""


# When Steps
@when(parsers.parse('the user searches for "{text}"'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
