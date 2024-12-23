from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.maximize_window()

# Get the size of the browser window
window_size = driver.get_window_size()

# Print the current size of the window
print(f"Current browser window size: Width = {window_size['width']}, Height = {window_size['height']}")

# Close the browser
driver.quit()