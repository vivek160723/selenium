import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()


driver.get("https://www.nopcommerce.com/en/demo")
btn=driver.find_element(By.XPATH,"//*[@id='ph-topic']/div[2]/div/div[1]/div[2]/div/div/a[2]")
time.sleep(3)
btn.click()
time.sleep(2)

driver.close()
time.sleep(5)
driver.quit()