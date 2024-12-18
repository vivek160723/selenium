# #BTES login page
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
#
# # Open the webpage
# driver.get("https://online.btes.co.in/login/index.php")
# try:
#     # logo = driver.find_elements(By.XPATH, "//img[@id='yui_3_17_2_1_1734504882959_20']")
#     login=driver.find_element(By.XPATH,"//input[@id='username']")
#     login.click()
#     login.send_keys("vivek@123")
#     time.sleep(2)
#     password = driver.find_element(By.XPATH, "//input[@id='password']")
#     password.click()
#     password.send_keys("Vivek@160723")
#     password.send_keys(Keys.RETURN)
#     print("Element located")
# except Exception as e:
#     print(e)
#
# time.sleep(3)
# driver.quit()
#

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://online.btes.co.in/login/index.php")

try:
    # Enter username
    login = driver.find_element(By.XPATH, "//input[@id='username']")
    login.click()
    login.send_keys("vivek@123")
    time.sleep(1)

    # Enter password
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.click()
    password.send_keys("Vivek@160723")
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    Set_button=driver.find_element(By.XPATH,"//*[@class='card-img dashboard-card-img']")
    Set_button.click()
    time.sleep(3)
    try:
        # Replace with an actual element unique to the dashboard or logged-in state
        dashboard_element = driver.find_element(By.XPATH, "//*[@class='navbar-inner']")
        print("Login successful. Dashboard element found.")
    except NoSuchElementException:
        print("Login failed. Dashboard element not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Close the browser
driver.quit()
