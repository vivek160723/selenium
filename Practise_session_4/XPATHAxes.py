from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://automationbookstore.dev")

#---------------------------------XPATH Axis--------------------------------------------------------
element_1=driver.find_element(By.XPATH,"//input[@id='username'])")
element_2=driver.find_element(By.XPATH,"//div[@class='container']/ancestor::*")
element_3=driver.find_element(By.XPATH,"//div[@class='container']/descendant::*")
element_4=driver.find_element(By.XPATH,"//button[@id='submit']/following-sibling::*")
element_5=driver.find_element(By.XPATH,"//label[@for='email']/preceding-sibling::*")

#---------------------------------------------------------------------------------------------------

element_1=driver.find_element(By.XPATH,"//input[@id='email' and @name='userEmail']")
element_2=driver.find_element(By.XPATH,"//button[@type='submit' and @class='btn-primary']")
element_3=driver.find_element(By.XPATH,"//a[@href='/home' or contains(text(), 'Home')]")

#------------------------contains()------------------------------------------------------------------

element_1=driver.find_element(By.XPATH,"///*[contains(@id, 'user')]")
element_2=driver.find_element(By.XPATH,"///button[contains(@class, 'submit-bia')] ")
element_3=driver.find_element(By.XPATH,"//p[contains(text(), 'Welcome')]")

#----------------------------Text()------------------------------------------------------------------

element_1=driver.find_element(By.XPATH,"//a[text()='About Us']")
element_2=driver.find_element(By.XPATH,"//span[text()='Submit Form']")

#----------------------------Starts-with()-----------------------------------------------------------

element_1=driver.find_element(By.XPATH,"//input[starts-with(@name, 'user')]")
element_2=driver.find_element(By.XPATH,"///div[starts-with(@id, 'main-')]")

#----------------------------Mixed Challenge()--------------------------------------------------------

element_1=driver.find_element(By.XPATH,"//section[@id='content']/descendant*[contains(@class, 'data')]")
element_2=driver.find_element(By.XPATH,"//h1[text()='Welcome']/following-sibling::*")
element_3=driver.find_element(By.XPATH,"//h1[text()='Welcome']/following-sibling::*[starts-with(name(), 'header')]")
element_4=driver.find_element(By.XPATH,"//p[text()='Disclaimer']/ancestor:😘")
element_5=driver.find_element(By.XPATH,"//input[starts-with(@name, 'email') and contains(@class, 'input')]")





