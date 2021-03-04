from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.reddit.com/')
print(driver.title)

'''Full Screenshot'''
# Only possible in headless mode is true.
s = lambda x: driver.execute_script("return document.body.parentNode.scroll" + x)
driver.set_window_size(s('Width'), s('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')

driver.quit()
