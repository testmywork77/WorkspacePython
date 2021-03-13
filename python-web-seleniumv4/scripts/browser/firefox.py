from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# In Selenium 4, executable_path has been deprecated,
# C:\\WebDrivers\\geckodriver.exe -Backward Slash, need escape character
# C:/WebDrivers/geckodriver.exe -Forward Slash, no need escape character
s = Service("C:/WebDrivers/geckodriver.exe")
driver = webdriver.Firefox(service=s)
print(type(driver))
driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
driver.quit()
