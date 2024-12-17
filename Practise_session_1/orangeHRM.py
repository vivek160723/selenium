import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://www.google.co.in")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("orangehrm login")
search_box.send_keys(Keys.RETURN)

time.sleep(2)
first_link = driver.find_element(By.XPATH, "(//h3)[1]")
first_link.click()

time.sleep(3)
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
login_button.click()

time.sleep(5)
driver.quit()
