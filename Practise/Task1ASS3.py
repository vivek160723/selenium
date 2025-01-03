from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the page
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

# Locate and interact with elements
driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("Doe")
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.ID, "datepicker").send_keys("12/29/2024")

# Select from dropdown
continent_dropdown = Select(driver.find_element(By.ID, "continents"))
continent_dropdown.select_by_visible_text("Europe")

# Submit the form
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Close the driver
driver.quit()
