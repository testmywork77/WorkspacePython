from selenium import webdriver


# C:\\WebDrivers\\geckodriver.exe -Backward Slash, need escape character
# C:/WebDrivers/geckodriver.exe -Forward Slash, no need escape character
driver = webdriver.Firefox(executable_path="C:/WebDrivers/geckodriver.exe")
print(type(driver))
driver.get("http://learn-automation.com")
myPageTitle = driver.title
print(myPageTitle)
assert "Automation - Selenium WebDriver tutorial Step by Step" in myPageTitle
driver.quit()
