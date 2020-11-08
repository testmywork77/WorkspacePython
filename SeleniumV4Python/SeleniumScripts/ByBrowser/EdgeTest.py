from selenium import webdriver
from selenium.webdriver.edge.service import Service


# In Selenium 4, executable_path has been deprecated,
# C:\\WebDrivers\\msedgedriver.exe -Backward Slash, need escape character
# C:/WebDrivers/msedgedriver.exe -Forward Slash, no need escape character
objService = Service("C:/WebDrivers/msedgedriver.exe")
driver = webdriver.Edge(service=objService)
print(type(driver))
driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
driver.quit()
