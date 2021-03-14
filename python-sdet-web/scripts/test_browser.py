# C:\\WebDrivers\\chromedriver.exe -Backward Slash, need escape character
# C:/WebDrivers/chromedriver.exe -Forward Slash, no need escape character
def test_browser(driver):
    assert "Google" in driver.title
    print(driver.title)
    print(driver.current_url)
    # driver.close()  # Only current window/child window will close
    driver.quit()  # Will close all the windows
