import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch the browser and navigate to the Facebook login page
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(3)

# 1. Self
self_element = driver.find_element(By.XPATH, "//*[@class='_6lux']/input")
print("Self Element Tag Name:", self_element.tag_name)

# 2. Child
child_element = driver.find_elements(By.XPATH, "//*[@class='_6lux']/child::*")
print("Child Element Tag Name:", len(child_element))

# 3. Parent
parent_element = driver.find_element(By.XPATH, "//*[@class='_6lux']/parent::*")
print("Parent Element Tag Name:", parent_element.tag_name)

# 4. Following
following_element = driver.find_element(By.XPATH, "//*[@class='_6lux']/following::*")
print("Following Element Tag Name:", following_element.tag_name)

# 5. Preceding
preceding_element = driver.find_elements(By.XPATH, "//*[@class='_6lux']/preceding::*")
print("Preceding Element Tag Name:", len(preceding_element))

# 6. Following-Sibling
following_sibling = driver.find_element(By.XPATH, "//*[@class='_6lux']/following-sibling::*")
print("Following Sibling Tag Name:", following_sibling.tag_name)

# 7. Preceding-Sibling
preceding_sibling = driver.find_element(By.XPATH, "//*[@class='_6lux']/preceding-sibling::*")
print("Preceding Sibling Tag Name:", preceding_sibling.tag_name)

# 8. Ancestor
ancestor_elements = driver.find_elements(By.XPATH, "//*[@class='_6lux']/ancestor::*")
print("Number of Ancestors:", len(ancestor_elements))
for idx, ancestor in enumerate(ancestor_elements, start=1):
    print(f"Ancestor {idx} - Tag Name: {ancestor.tag_name}, Class Name: {ancestor.get_attribute('class')}")

# Close the browser
driver.quit()