import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://text-compare.com")

driver.find_element(By.XPATH,"//*[@id='inputText1']").send_keys("Vivek")

act=ActionChains(driver)

act.key_down(Keys.COMMAND)
act.send_keys("a")
act.key_up(Keys.COMMAND)
act.perform()
time.sleep(3)

act.key_down(Keys.COMMAND)
act.send_keys("c")
act.key_up(Keys.COMMAND)
act.perform()
time.sleep(3)

act.send_keys(Keys.TAB).perform()

act.key_down(Keys.COMMAND)
act.send_keys("v")
act.key_up(Keys.COMMAND)
act.perform()
time.sleep(5)
