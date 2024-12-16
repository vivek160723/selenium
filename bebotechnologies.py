from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize Safari WebDriver
driver = webdriver.Safari()

# Navigate to the Google homepage
driver.get("https://www.google.co.in")

# Locate the search bar using its name attribute
search_bar = driver.find_element(By.NAME, "q")

# Enter the search query and simulate pressing the Enter key
search_bar.send_keys("bebotechnologies" + Keys.RETURN)

# Wait for a few seconds to see the results (optional, for debugging purposes)
import time
time.sleep(5)

# Quit the browser
driver.quit()
