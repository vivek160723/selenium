from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://demo.guru99.com/test/newtours/")

try:
    username = driver.find_element(By.NAME, "userName")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("testuser")
    password.send_keys("testpassword")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='submit' and @value='Submit']")
    submit_button.click()
    print("Submit button clicked successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(3)
driver.quit()
