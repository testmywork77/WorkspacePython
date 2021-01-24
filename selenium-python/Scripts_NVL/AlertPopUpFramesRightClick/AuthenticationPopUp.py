from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

# http://admin:admin@the-internet.herokuapp.com/basic_auth
# http://the-internet.herokuapp.com/basic_auth
driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')

time.sleep(3)
driver.close()
