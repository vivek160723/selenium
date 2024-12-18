from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the Amazon webpage
driver.get("https://www.amazon.in")

try:
    # Locate the search box using a dynamic XPath that matches its attributes
    search_box = driver.find_element(By.XPATH, "//input[contains(@id, 'twotabsearchtextbox')]")

    # Enter 'laptops' in the search box and press Enter
    search_box.click()
    search_box.send_keys("laptops")
    search_box.send_keys(Keys.RETURN)
    print("Search for 'laptops' executed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for a few seconds to observe the results
time.sleep(5)

# Close the browser
driver.quit()
