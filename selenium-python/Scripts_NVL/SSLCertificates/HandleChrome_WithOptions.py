from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.add_argument('--allow-running-insecure-content')
opt.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://expired.badssl.com/") # Intentionally commented- only testing purpose
driver.get("https://google.com/")

time.sleep(3)
driver.close()
