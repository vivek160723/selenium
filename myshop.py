import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
Top_menu=driver.find_elements(By.CLASS_NAME,"sf-menu")

for i in Top_menu:
    print(i.text)

driver.quit()



