from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://amazon.in")

wait = WebDriverWait(driver, 10)
expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
wait.until(ec.title_is(expected_title))
print(driver.title)

# best_sellers = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Best Sellers')))
# driver.execute_script("arguments[0].click();", best_sellers)

# driver.execute_script("history.go(0);")

inner_text = driver.execute_script("return document.documentElement.innerText")
print(inner_text)

time.sleep(3)
driver.close()
