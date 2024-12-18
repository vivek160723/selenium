from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.guru99.com/test/newtours/")

try:
    register_link = driver.find_element(By.XPATH, "//a[text()='REGISTER']")
    register_link.click()
    print("Clicked on the REGISTER link successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(3)
driver.quit()
