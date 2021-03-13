import pytest

from pytest_bdd import given
from selenium import webdriver

# Constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()


# Shared Given Steps
@given('the home page is displayed', target_fixture='ddg_home')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)