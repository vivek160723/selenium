from selenium import webdriver

# Initialize the WebDriver (e.g., Chrome in this case)
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.amazon.in/")

# Retrieve the page source
page_source = driver.page_source

# Print the page source
print("Page source retrieved successfully.")
print(page_source)

# Close the browser
driver.quit()