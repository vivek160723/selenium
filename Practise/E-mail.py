from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Safari()

# Step 1: Open Gmail
driver.get("https://mail.google.com")

# Step 2: Locate the email input field and enter your email
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("chaudharyvivek250103@gmail.com")  # Replace with your Gmail address
email_field.send_keys(Keys.RETURN)

# Wait for the password page to load
time.sleep(3)

# Step 3: Locate the password input field and enter your password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("pnzlxfcupryrnoka")  # Replace with your Gmail password
password_field.send_keys(Keys.RETURN)

# Wait for the inbox to load
time.sleep(5)

# Optional: Close the browser after observing the result
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Safari()

# Step 1: Open Gmail
driver.get("https://mail.google.com")

# Step 2: Enter email
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)
email_field.send_keys("chaudharyvivek250103@gmail.com")
email_field.send_keys(Keys.RETURN)

# Step 3: Enter password
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_field.send_keys("pnzlxfcupryrnoka")
password_field.send_keys(Keys.RETURN)

# Step 4: Wait for inbox to load
time.sleep(5)

# Optional: Close the browser
driver.quit()
