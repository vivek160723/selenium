import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://www.selenium.dev/documentation/")
search_box=driver.find_element(By.PARTIAL_LINK_TEXT,"Driver")
search_box.click()
search_box2=driver.find_element(By.LINK_TEXT,"Actions API")
search_box2.click()
time.sleep(3)

driver.quit()