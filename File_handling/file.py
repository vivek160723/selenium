import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

location=os.getcwd()
def chrome_setup():
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(options=ops)
    return driver

driver=chrome_setup()
driver.get("https://github.com/SeleniumHQ/selenium-ide/releases")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='d-flex flex-justify-start col-12 col-lg-9']/a/span[2]").click()
time.sleep(5)
