# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
#
# d=webdriver.Chrome()
# d.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
#
# Comp=d.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[2]/li[1]/a")
# notebook=d.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a")
#
#
# act=ActionChains(d)
# act.move_to_element(Comp).move_to_element(notebook).click().perform()
# time.sleep(5)
#


import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

computer=driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[1]/a")
notebook=driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a")

act=ActionChains(driver)

act.move_to_element(computer).move_to_element(notebook).click().perform()
time.sleep(3)
