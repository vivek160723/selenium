from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Safari WebDriver
driver = webdriver.Safari()

# Navigate to the Google homepage
driver.get("https://www.google.co.in")

# Locate the search bar using its name attribute
search_bar = driver.find_element(By.NAME, "q")

# Enter the search query and simulate pressing the Enter key
search_bar.send_keys("bebotechnologies" + Keys.RETURN)

# Wait for the search results to load
time.sleep(3)

# Locate the first search result link and click it
try:
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")  # Locate the first result by the header (h3)
    first_result.click()  # Simulate clicking the first result
    print("Opened the first search result.")
except Exception as e:
    print(f"Error: {e}")

# Wait for a few seconds to view the opened site
time.sleep(5)

# Quit the browser
driver.quit()
