
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)

Right_click=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
notebook=driver.find_element(By.XPATH,"/html/body/ul/li[3]/span")

act=ActionChains(driver)

act.context_click(Right_click).context_click(notebook).click().perform()
time.sleep(3)
alert=driver.switch_to.alert
print(alert.text)
alert.dismiss()
