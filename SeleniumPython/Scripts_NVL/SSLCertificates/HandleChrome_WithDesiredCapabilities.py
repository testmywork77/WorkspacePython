from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import time

# ***Desired Capabilities ***
dc = DesiredCapabilities().CHROME.copy()
dc['acceptInsecureCerts'] = True

driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=dc)
driver.implicitly_wait(10)
driver.maximize_window()
# driver.get("https://expired.badssl.com/")  # Intentionally commented- only testing purpose
driver.get("https://google.com/")
driver.maximize_window()

time.sleep(3)
driver.close()
