# <input type="text" class="inputtext _55r1 _6luy" name="email" id="email"
# data-testid="royal_email" placeholder="Email address or phone number"
# autofocus="1" aria-label="Email address or phone number">

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
try:
    # username = driver.find_element(By.XPATH, "//input[@class='inputtext _55r1 _6luy' and @name='email']")
    username = driver.find_element(By.XPATH, "//input[@class='inputtext _55r1 _6luy' or @id='email']")
    # username=driver.find_element(By.XPATH,"//input[contains(@id,'email')]")
    username.send_keys("vivek@gmail.com")
    time.sleep(3)
    print("username Successfull")
except Exception as e:
    print("Done")
try:
    password = driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]") #by using tag ,class and attribute
    # password = driver.find_element(By.CSS_SELECTOR, "input[name=pass]") # by using tag and attriute
    password = driver.find_Element(By.XPATH,"//input[starts-with(@name,'password')]")
    password.send_keys("12345678")
    time.sleep(3)
    print("password successfull")
except Exception as e:
    print(e)
# Close the driver
driver.close()
