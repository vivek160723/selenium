# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# username_field = driver.find_element(By.NAME, "username")
# username_field.send_keys("Admin")
#
# password_field = driver.find_element(By.NAME, "password")
# password_field.send_keys("admin123")
#
# login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
# login_button.click()
#
# driver.quit()
############### Explicit ##################
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome()
driver.get("https://www.google.com/")
sb=driver.find_element(By.NAME,"q")
sb.send_keys("Selenium")
sb.send_keys(Keys.RETURN)
wait=WebDriverWait(driver,2)
wait=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='gNO89b']")))