import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://demoqa.com/automation-practice-form")


input_boxes = driver.find_elements(By.TAG_NAME, "input")
print(len(input_boxes))
for box in input_boxes:
    value = box.get_attribute("value")
    print(value)

time.sleep(3)
driver.quit()
