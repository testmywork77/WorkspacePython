from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
import time


dc = DesiredCapabilities.FIREFOX.copy()
dc['acceptInsecureCerts'] = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), capabilities=dc)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://expired.badssl.com/")  # Intentionally commented- only testing purpose
# driver.get("https://google.com/")

time.sleep(3)
driver.close()
