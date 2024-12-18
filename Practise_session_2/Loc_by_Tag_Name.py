import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the webpage
driver.get("https://demoqa.com/automation-practice-form")

# Find all input elements
input_boxes = driver.find_elements(By.TAG_NAME, "input")
print(f"Total input fields found: {len(input_boxes)}")

# Loop through each input box
for box in input_boxes:
    name = box.get_attribute("name")  # Get the name attribute
    value = box.get_attribute("value")  # Get the value attribute
    print(f"Input Name: {name}, Value: {value}")

# Pause for 3 seconds and close the browser
time.sleep(3)
driver.quit()
