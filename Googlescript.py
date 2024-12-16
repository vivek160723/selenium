import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver=webdriver.Safari()
# driver.get("https://www.google.co.in")
#
# time.sleep(5)
# driver.quit()

###################################--TO search on the search bar--######################################
driver=webdriver.Safari()
driver.get("https://www.google.co.in")

search_Box = driver.find_element(By.NAME,"q")
search_Box.send_keys("instagram")
search_Box.send_keys(Keys.RETURN)
time.sleep(3)

first_link = driver.find_element(By.XPATH,"(//h3)[1]")

first_link.click()
time.sleep(3)
driver.quit()


