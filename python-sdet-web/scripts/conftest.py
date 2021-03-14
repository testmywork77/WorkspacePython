# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
#
#
# @pytest.fixture
# def driver():
#     browser = "chrome"
#     if browser == "chrome":
#         driver = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver.exe")
#     elif browser == "firefox":
#         driver = webdriver.Firefox(executable_path="C:/WebDrivers/geckodriver.exe")
#     elif browser == "edge":
#         driver = webdriver.Edge(executable_path="C:/WebDrivers/msedgedriver.exe")
#     # if browser == "chrome":
#     #     driver = webdriver.Chrome(ChromeDriverManager().install())
#     # elif browser == "firefox":
#     #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     # elif browser == "ie":
#     #     driver = webdriver.Ie(IEDriverManager().install())
#     # elif browser == "edge":
#     #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     else:
#         print(f"please pass the browser name: {browser}")
#         raise Exception("driver not found")
#     print(type(driver))
#     driver.get("http://www.google.com")
#     driver.maximize_window()
#     return driver
