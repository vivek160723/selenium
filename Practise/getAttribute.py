import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()


driver.get("https://demoqa.com/automation-practice-form")

input_boxes = driver.find_elements(By.TAG_NAME, "input")
print(f"Total input fields found: {len(input_boxes)}")

for box in input_boxes:
    name = box.get_attribute("name")
    print(f"Input Name: {name}")

time.sleep(3)
driver.quit()
