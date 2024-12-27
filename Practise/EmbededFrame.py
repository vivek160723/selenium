import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://demo.automationtesting.in/Frames.html")

    btn1 = driver.find_element(By.XPATH, "//a[@href='#Multiple']")
    btn1.click()
    time.sleep(1)

    outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
    driver.switch_to.frame(outer_frame)

    inner_frame = driver.find_element(By.XPATH, "//iframe")
    driver.switch_to.frame(inner_frame)

    input_box = driver.find_element(By.XPATH, "//input[@type='text']")
    input_box.send_keys("vivek")
    time.sleep(3)
finally:
    driver.quit()