from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.reddit.com/')
print(driver.title)
driver.get_screenshot_as_file('reddit_1.png')
driver.quit()
