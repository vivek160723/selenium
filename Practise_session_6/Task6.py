###conditional commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

try:
    button = driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")

    if button.is_enabled():
        print("The button is enabled. Proceeding to click.")
        button.click()
    else:
        print("The button is disabled. Cannot click.")
except NoSuchElementException:
    print("The button element was not found on the page.")

driver.quit()