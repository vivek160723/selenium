from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

driver.refresh()

print("The webpage has been refreshed.")

# Close the browser
driver.quit()