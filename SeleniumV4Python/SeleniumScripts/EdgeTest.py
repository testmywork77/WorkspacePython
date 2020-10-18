from selenium import webdriver


# C:\\WebDrivers\\msedgedriver.exe -Backward Slash, need escape character
# C:/WebDrivers/msedgedriver.exe -Forward Slash, no need escape character
driver = webdriver.Edge(executable_path="C:/WebDrivers/msedgedriver.exe")
print(type(driver))
driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
driver.quit()
