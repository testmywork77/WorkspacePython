from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# In Selenium 4, executable_path has been deprecated,
# C:\\WebDrivers\\chromedriver.exe -Backward Slash, need escape character
# C:/WebDrivers/chromedriver.exe -Forward Slash, no need escape character
objService = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=objService)
print(type(driver))

driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)

assert "Google" in myPageTitle
driver.quit()
