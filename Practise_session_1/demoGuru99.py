import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com")

time.sleep(3)
driver.quit()