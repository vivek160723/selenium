import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Facebook login page
driver.get("https://en-gb.facebook.com/login/")
try:
    username = driver.find_element(By.CSS_SELECTOR, "input#email")
    username.send_keys("vivek")
    time.sleep(3)
    print("username Successfull")
except Exception as e:
    print("Done")
try:
    password = driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]") #by using tag ,class and attribute
    # password = driver.find_element(By.CSS_SELECTOR, "input[name=pass]") # by using tag and attriute
    password.send_keys("12345678")
    time.sleep(3)
    print("password successfull")
except Exception as e:
    print(e)
# Close the driver
driver.close()
