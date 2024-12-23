from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

current_url = driver.current_url
print(f"Current URL: {current_url}")

expected_url = "https://www.amazon.in/"

if current_url == expected_url:
    print("The current URL matches the expected URL.")
else:
    print("The current URL does NOT match the expected URL.")

# Close the browser
driver.quit()