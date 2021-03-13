# Explicit Wait- presence_of_elements_located
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get('https://www.freshworks.com/')
driver.maximize_window()

footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for link in footer_links:
    print(link.text)

driver.close()
