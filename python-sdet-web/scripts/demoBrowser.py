from selenium import webdriver

browser = "chrome"
if browser == "chrome":
    driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
elif browser == "firefox":
    driver = webdriver.Firefox(executable_path="C:/WebDrivers/geckodriver.exe")
elif browser == "edge":
    driver = webdriver.Edge(executable_path="C:/WebDrivers/msedgedriver.exe")
else:
    print(f"please pass the browser name: {browser}")
    raise Exception("driver not found")
print(type(driver))
driver.get("http://www.google.com")
driver.maximize_window()
assert "Google" in driver.title
print(driver.title)
print(driver.current_url)
# driver.close()  # Only current window/child window will close
driver.quit()  # Will close all the windows
