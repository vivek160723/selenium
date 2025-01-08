from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(3)

table = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table")
rows = table.find_elements(By.XPATH, ".//tr")

for row_index, row in enumerate(rows):
    cells = row.find_elements(By.XPATH, ".//th | .//td")
    row_data = [cell.text for cell in cells]
    print(f"Row {row_index + 1}: {row_data}")

time.sleep(3)
driver.quit()