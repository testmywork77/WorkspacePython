from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opts = Options()
opts.set_capability('acceptInsecureCerts', True)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
driver.implicitly_wait(10)
driver.maximize_window()
# driver.get("https://expired.badssl.com/")  # Intentionally commented- only testing purpose
driver.get("https://google.com/")

time.sleep(3)
driver.close()
