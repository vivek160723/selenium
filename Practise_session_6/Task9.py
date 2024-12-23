from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Initialize the WebDriver (e.g., Chrome in this case)
driver = webdriver.Safari()

# Navigate to the target webpage
driver.get("https://www.amazon.in")

try:
    heading = driver.find_element(By.XPATH, "//*[@id='glow-ingress-line2']")
    expected_text = " 'Update location' "

    if heading.text == expected_text:
        print("The heading text is correct.")
    else:
        print(f"The heading text is incorrect. Found: '{heading.text}', Expected: '{expected_text}'")
except NoSuchElementException:
    print("The heading element was not found on the page.")

# Close the browser
driver.quit()