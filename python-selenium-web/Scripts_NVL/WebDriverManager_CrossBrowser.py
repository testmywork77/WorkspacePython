from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
import time

browserName = "firefox"  # "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "ie":
    driver = webdriver.Ie(IEDriverManager().install())
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print(f"please pass the browser name: {browserName}")
    raise Exception("driver not found")

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("naveenanimation30@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Test@12345")
driver.find_element(By.ID, 'loginBtn').click()

time.sleep(5)
driver.quit()

