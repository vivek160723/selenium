import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.orangehrm.com")
time.sleep(3)

element_1=driver.find_element(By.XPATH,"/html/body/div/div/div/section[1]/div[3]")
driver.get_screenshot_as_file(os.getcwd()+"/screenSHOT.png")

driver.quit()
