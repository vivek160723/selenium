from selenium import webdriver

# Initialize the WebDriver (e.g., Chrome in this case)
driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

page_title = driver.title
print(page_title)
keyword = "Online Shopping"

if keyword in page_title:
    print(f"The webpage is loaded correctly. Title contains the keyword: '{keyword}'")
else:
    print(f"The webpage is NOT loaded correctly. Title does not contain the keyword: '{keyword}'")

driver.quit()