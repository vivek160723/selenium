import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.implicitly_wait(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(4)
winds=driver.window_handles
print(winds)
print(len(winds))
print(type(winds))

for i in winds:
    driver.switch_to.window(i)
    print(driver.title)


