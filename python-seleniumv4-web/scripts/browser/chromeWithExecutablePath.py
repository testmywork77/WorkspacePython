from selenium import webdriver


# C:\\WebDrivers\\chromedriver.exe -Backward Slash, need escape character
# C:/WebDrivers/chromedriver.exe -Forward Slash, no need escape character
driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
print(type(driver))
driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
driver.quit()
