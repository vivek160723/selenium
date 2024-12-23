

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Safari()


driver.get("https://www.amazon.in")

try:
    element = driver.find_element(By.XPATH, "//*[@id='nav-logo-sprites']")


    if element.is_displayed():
        print("The element is displayed on the page.")
    else:
        print("The element is NOT displayed on the page.")
except NoSuchElementException:
    print("The element was not found on the page.")

driver.quit()