from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")

try:
    email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
    email_input.click()
    email_input.send_keys("testemail@example.com")
    print("Email address entered successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(3)

# Close the browser
driver.quit()
