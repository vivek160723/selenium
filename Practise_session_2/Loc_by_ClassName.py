import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://www.selenium.dev")
search_box=driver.find_elements(By.CLASS_NAME,"nav-link")
time.sleep(3)
search_box[3].click()
time.sleep(3)

driver.quit()