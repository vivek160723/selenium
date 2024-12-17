import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://www.google.co.in")
search_box=driver.find_element(By.NAME,"q")

search_box.send_keys("Python programming language")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

driver.quit()