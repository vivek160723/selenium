from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(3)

table = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table")

rows = table.find_elements(By.XPATH, ".//tr")
num_rows = len(rows)

columns = rows[0].find_elements(By.XPATH, ".//th | .//td")
num_columns = len(columns)

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

time.sleep(3)

driver.quit()