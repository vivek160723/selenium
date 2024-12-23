from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://www.w3schools.com/html/html_forms.asp")

try:
    checkbox = driver.find_element(By.XPATH, "//*[@id='css']")
    if checkbox.is_selected():
        print("The checkbox is selected.")
    else:
        print("The checkbox is NOT selected.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()