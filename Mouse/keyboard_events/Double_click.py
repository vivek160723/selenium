import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
time.sleep(5)

f1=driver.find_element(By.XPATH,'//iframe[@id="iframeResult"]')
driver.switch_to.frame(f1)
time.sleep(5)

text1=driver.find_element(By.XPATH,'//input[@id="field1"]')
time.sleep(3)
text1.clear()
time.sleep(3)
text1.send_keys("hello Mansi")
time.sleep(5)


# time.sleep(5)

obj=ActionChains(driver)

btn=driver.find_element(By.XPATH,'//button[@ondblclick="myFunction()"]')
obj.double_click(btn).perform()
time.sleep(5)

#------------validation
t1=driver.find_element(By.XPATH,'//input[@id="field1"]').get_attribute("value")

t2=driver.find_element(By.XPATH,'//input[@id="field2"]').get_attribute("value")
# print(t1)
# print(t2)

if t1==t2:
    print("Pass")
else:
    print("Fail")