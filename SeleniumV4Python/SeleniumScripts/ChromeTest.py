from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# To supress this warning: DeprecationWarning: executable_path has been deprecated,
# please pass in a Service object driver = webdriver.Edge(executable_path="C:/WebDrivers/msedgedriver.exe")
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
