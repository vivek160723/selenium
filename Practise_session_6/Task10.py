from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# @##################this is incomplete code



# Initialize the WebDriver (e.g., Chrome in this case)

driver = webdriver.Safari()

driver.get("https://www.amazon.in")

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])


driver.get("https://www.google.com")

# Print the title of the current tab
print(f"Current tab title: {driver.title}")

# Close the browser
driver.quit()