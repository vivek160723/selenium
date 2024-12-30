from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
time.sleep(3)

first_frame = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
driver.switch_to.frame(first_frame)

inputBox = driver.find_element(By.XPATH, "//*[@id='datepicker']")
inputBox.click()

target_month = "October"
target_year = "2025"
din="20"
while True:
    month = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text
    year = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text

    if month == target_month and year == target_year:
        break

    next_button = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span")
    next_button.click()
    time.sleep(1)

days = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
for i in days:
    if i.text==din:
        i.click()

time.sleep(3)
driver.quit()