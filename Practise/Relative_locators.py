from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome()

driver.get("https://automationbookstore.dev")

element_Below=driver.find_element(locate_with(By.TAG_NAME,"li").below({By.ID: "pid1_title"})).text
print(element_Below)
element_right=driver.find_element(locate_with(By.TAG_NAME,"li").to_right_of({By.ID: "pid1_title"})).text
print(element_right)
element_left=driver.find_element(locate_with(By.TAG_NAME,"h2").to_left_of({By.ID: "pid2_title"})).text
print(element_left)
element_above=driver.find_element(locate_with(By.TAG_NAME,"h2").above({By.ID: "pid5_title"})).text
print(element_above)
driver.quit()