import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

# try:
#     driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#     driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()
#     alert = driver.switch_to.alert
#     time.sleep(3)
#     alert.accept()
#
#     result = driver.find_element(By.XPATH, "//*[@id='result']")
#     expected = "You clicked: Ok"
#
#     if result.text == expected:
#         print("You clicked Ok")
#     else:
#         print("You cancelled")
# finally:
#     driver.quit()

#######################################################################################

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()

    alert = driver.switch_to.alert
    time.sleep(3)
    alert.send_keys("Badmash")
    alert.accept()

    result = driver.find_element(By.XPATH, "//*[@id='result']")
    expected = "You entered: Badmash"

    if result.text == expected:
        print("You entered: Badmash")
    else:
        print("You cancelled")
finally:
    driver.quit()