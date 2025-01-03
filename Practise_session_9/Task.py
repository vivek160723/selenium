# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Set up the WebDriver (ensure you have the correct driver for your browser)
# driver = webdriver.Chrome()
#
# try:
#     # Navigate to the demo site
#     driver.get("https://www.globalsqa.com/demo-site/datepicker/#lcon%20Trigger")
#
#     # Maximize the browser window
#     driver.maximize_window()
#     time.sleep(2)
#
#     # Switch to the iframe containing the date picker
#     iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
#     driver.switch_to.frame(iframe)
#
#     # Open the date picker by clicking on the input field
#     date_picker = driver.find_element(By.ID, "datepicker")
#     date_picker.click()
#
#     # Select the "15th" of the current month
#     # Locate the table and click the desired date
#     dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
#     for date in dates:
#         if date.text == "15":
#             date.click()
#             break
#
#     # Wait to observe the result
#     time.sleep(2)
#
# finally:
#     # Close the browser
#     driver.quit()
###############################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Set up WebDriver (ensure you have the correct driver for your browser)
# driver = webdriver.Chrome()
#
# try:
#     # Navigate to the demo site
#     driver.get("https://www.globalsqa.com/demo-site/datepicker/#lcon%20Trigger")
#
#     # Maximize the browser window
#     driver.maximize_window()
#     time.sleep(2)
#
#     # Switch to the iframe containing the date picker
#     iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
#     driver.switch_to.frame(iframe)
#
#     # Open the date picker by clicking on the input field
#     date_picker = driver.find_element(By.ID, "datepicker")
#     date_picker.click()
#
#     # Target date
#     target_year = 2025
#     target_month = "December"
#     target_day = "25"
#
#     # Navigate through the months and years
#     while True:
#         # Get the current displayed month and year
#         displayed_month_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-title").text
#         displayed_month, displayed_year = displayed_month_year.split()
#         displayed_year = int(displayed_year)
#
#         # Check if the target month and year are displayed
#         if displayed_year == target_year and displayed_month == target_month:
#             break
#
#         # Navigate to the next month if the target year/month is ahead
#         next_button = driver.find_element(By.CLASS_NAME, "ui-datepicker-next")
#         next_button.click()
#         time.sleep(0.5)  # Add a short delay to allow the UI to update
#
#     # Select the target day
#     dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
#     for date in dates:
#         if date.text == target_day:
#             date.click()
#             break
#
#     # Wait to observe the result
#     time.sleep(2)
#
# finally:
#     # Close the browser
#     driver.quit()

######################################## not working ###################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver (ensure you have the correct driver for your browser)
driver = webdriver.Chrome()

try:
    # Navigate to the demo site
    driver.get("https://vitalets.github.io/bootstrap-datepicker/")

    # Maximize the browser window
    driver.maximize_window()
    time.sleep(2)

    # Locate the date picker input field
    date_input = driver.find_element(By.CLASS_NAME, "datepicker")

    # Enter the desired date
    target_date = "01/01/2024"
    date_input.clear()
    date_input.send_keys(target_date)
    time.sleep(1)  # Allow some time for the input to register

    # Retrieve the value from the input field to verify
    updated_date = date_input.get_attribute("value")
    if updated_date == target_date:
        print("Date updated successfully: ", updated_date)
    else:
        print("Date update failed. Current value: ", updated_date)

    # Wait to observe the result
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
