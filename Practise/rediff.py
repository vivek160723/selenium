import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# search_Box = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr/td[1]/a") #self
# length = len(search_Box)
search_Box2 = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[1]/td[3]/following-sibling::td") #self
length2 = len(search_Box2)
print(length2)
for i in search_Box2:
    print(i.text)
# Close the WebDriver
driver.quit()