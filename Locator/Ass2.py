from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver and navigate to the URL
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")

# Question 1: Locate search bar by ID and submit search
search_bar = driver.find_element(By.ID, "search_query_top")
search_bar.send_keys("search box")
search_bar.submit()

# Question 2: Locate search input using name attribute and submit search
search_input = driver.find_element(By.NAME, "search_query")
search_input.send_keys("Selenium testing")
search_input.send_keys(Keys.RETURN)

# Question 3: Locate "Sign In" button using class name and click it
sign_in_button = driver.find_element(By.CLASS_NAME, "login")
sign_in_button.click()

# Navigate back for further actions
driver.back()

# Question 4: Locate first <h1> by tag name and print its text
heading = driver.find_element(By.TAG_NAME, "h1")
print("Heading text:", heading.text)

# Question 5: Locate "Contact Us" link by visible text and click it
contact_us_link = driver.find_element(By.LINK_TEXT, "Contact us")
contact_us_link.click()

# Navigate back for further actions
driver.back()

# Question 6: Locate "Contact Us" link using partial link text and click it
partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Contact")
partial_link.click()

# Navigate back for further actions
driver.back()

# Question 7: Locate button using CSS Selector and click it
try:
    button = driver.find_element(By.CSS_SELECTOR, "#submit_button.class_name")
    button.click()
except Exception as e:
    print("Button not found or action failed:", e)

# Navigate back for further actions
driver.back()

# Question 8: Locate "Follow us on Facebook" link using XPath and click it
facebook_link = driver.find_element(By.XPATH, "//a[@title='Facebook']")
facebook_link.click()

# Navigate back for further actions
driver.back()

# Question 9: Combine CSS Selector for parent and XPath for child element
try:
    parent = driver.find_element(By.CSS_SELECTOR, ".parent_class")
    child = parent.find_element(By.XPATH, ".//child_tag[@attribute='value']")
    child.click()
except Exception as e:
    print("Parent or child element not found:", e)

# Close the browser
driver.quit()
