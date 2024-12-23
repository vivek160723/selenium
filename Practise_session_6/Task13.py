import time

from selenium import webdriver


driver = webdriver.Safari()


driver.get("https://www.amazon.in")
time.sleep(2)
driver.forward()
driver.get("https://www.flipkart.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.quit()