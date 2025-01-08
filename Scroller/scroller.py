import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://tailwindcss.com")
driver.implicitly_wait(3)
driver.maximize_window()

driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(10)


