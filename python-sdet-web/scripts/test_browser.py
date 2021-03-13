from selenium import webdriver


# C:\\WebDrivers\\chromedriver.exe -Backward Slash, need escape character
# C:/WebDrivers/chromedriver.exe -Forward Slash, no need escape character
def test_browser():
    browser = "edge"
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
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.back()
    driver.refresh()
    # driver.close()  # Only current window/child window will close
    driver.quit()  # Will close all the windows
