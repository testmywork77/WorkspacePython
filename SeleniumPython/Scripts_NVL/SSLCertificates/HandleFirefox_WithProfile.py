from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time


profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://expired.badssl.com/")  # Intentionally commented- only testing purpose
driver.get("https://google.com/")

time.sleep(3)
driver.close()
