# *******************************Python_Selenium**********************************************

# *** WebDriverBasics.py ***
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	import time

	driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe")
	driver.implicitly_wait(5)
	driver.get("http://www.google.com")
	driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
	elementList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

	for element in elementList:
		print(element.text)
		if element.text == 'naveen automationlabs youtube':
			element.click()
			break

	time.sleep(5)
	driver.quit()
	
# ***WebDriverManager_CrossBrowser.py:***
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	import time
	from webdriver_manager.chrome import ChromeDriverManager
	from webdriver_manager.firefox import GeckoDriverManager
	from webdriver_manager.microsoft import IEDriverManager
	from webdriver_manager.microsoft import EdgeChromiumDriverManager

	browserName = "edge"

	if browserName == "chrome":
		driver = webdriver.Chrome(ChromeDriverManager().install())
	elif browserName == "firefox":
		driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
	elif browserName == "ie":
		driver = webdriver.Ie(IEDriverManager().install())
	elif browserName == "edge":
		driver = webdriver.Edge(EdgeChromiumDriverManager().install())
	else:
		print(f"Please pass the correct browser name: {browserName}")
		raise Exception("Driver is not found!")

	driver.implicitly_wait(5)
	driver.get("https://opensource-demo.orangehrmlive.com/")
	assert driver.title == "OrangeHRM"

	driver.find_element(By.ID, "txtUsername").send_keys("Admin")
	driver.find_element(By.ID, "txtPassword").send_keys("admin123")
	driver.find_element(By.ID, "btnLogin").click()
	assert driver.title == "OrangeHRM"

	time.sleep(5)
	driver.quit()
	


