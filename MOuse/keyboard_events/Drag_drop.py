import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(2)


oslo=driver.find_element(By.XPATH,"//*[@id='box1']")
wash=driver.find_element(By.XPATH,"//*[@id='box3']")
Stock=driver.find_element(By.XPATH,"//*[@id='box2']")
copen=driver.find_element(By.XPATH,"//*[@id='box4']")
seoul=driver.find_element(By.XPATH,"//*[@id='box5']")
Rome=driver.find_element(By.XPATH,"//*[@id='box6']")
madr=driver.find_element(By.XPATH,"//*[@id='box7']")

trgt1=driver.find_element(By.XPATH,"//*[@id='box101']")
trgt2=driver.find_element(By.XPATH,"//*[@id='box103']")
trgt3=driver.find_element(By.XPATH,"//*[@id='box102']")
trgt4=driver.find_element(By.XPATH,"//*[@id='box104']")
trgt5=driver.find_element(By.XPATH,"//*[@id='box105']")
trgt6=driver.find_element(By.XPATH,"//*[@id='box106']")
trgt7=driver.find_element(By.XPATH,"//*[@id='box107']")

act=ActionChains(driver)
act.drag_and_drop(oslo,trgt1).perform()
act.drag_and_drop(wash,trgt2).perform()
act.drag_and_drop(Stock,trgt3).perform()
act.drag_and_drop(copen,trgt4).perform()
act.drag_and_drop(seoul,trgt5).perform()
act.drag_and_drop(Rome,trgt6).perform()
act.drag_and_drop(madr,trgt7).perform()


time.sleep(3)
assert "box1" in trgt1.get_attribute("innerHTML"), "Oslo failed"
assert "box3" in trgt2.get_attribute("innerHTML"), "Washington failed"
