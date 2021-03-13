# JavaScript Execute Script's Scroll- Top to Bottom and Bottom to Top
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://amazon.in")

trendDeals_link = driver.find_element(By.XPATH, "//span[contains(.,'Trending Deals')]")
print(trendDeals_link.text)
driver.execute_script("arguments[0].scrollIntoView(true);", trendDeals_link)

time.sleep(5)
driver.close()
