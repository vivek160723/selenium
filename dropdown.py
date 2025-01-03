from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Safari WebDriver
driver = webdriver.Safari()
try:
    # Open the target webpage
    driver.get("https://testautomationpractice.blogspot.com/")

    # Wait until the dropdown is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='country']"))
    )

    # Locate the dropdown element
    dropdown = driver.find_element(By.XPATH, "//*[@id='country']")

    # Create a Select object
    select = Select(dropdown)

    # Print all available options
    print("Available options in the dropdown:")
    for option in select.options:
        print(option.text.strip())

    select.select_by_index(3)

    # Print the selected option
    selected_option = select.first_selected_option
    print(f"Selected option: {selected_option.text.strip()}")

finally:
    driver.quit()