import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://www.orangehrm.com")
print(driver.current_url)
print(driver.title)
print(driver.page_source)



driver.quit()
