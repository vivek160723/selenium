from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.co.in")

page_title = driver.title
print(f"The title of the webpage is: '{page_title}'")

# Close the browser
driver.quit()