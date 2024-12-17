import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")

time.sleep(2)

# images_total=driver.find_elements(By.TAG_NAME,"a")
# print(len(images_total))      //to find the total number of images




driver.quit()



