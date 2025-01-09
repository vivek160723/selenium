import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Connect to MySQL database using pymysql
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="vivek@160723",
    database="Selenium"
)
cursor = db_connection.cursor()

driver = webdriver.Chrome()
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")

wait = WebDriverWait(driver, 20)  # Increased wait time

# Fetch data from MySQL
cursor.execute("SELECT InitialDepositAmount, InterestRate, LengthOfCD_Months, Compounding FROM CertificatesOfDeposit")
rows = cursor.fetchall()

for row in rows:
    try:
        initial_deposit, interest_rate, length_of_cd, compounding = row

        # Input the initial deposit amount
        deposit_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']")))
        deposit_field.clear()
        deposit_field.send_keys(str(initial_deposit))

        time.sleep(1)

        # Input the interest rate
        rate_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mat-input-2']")))
        rate_field.clear()
        rate_field.send_keys(str(interest_rate))

        time.sleep(1)

        # Input the length of CD (converted to years if necessary)
        tenure_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']")))
        tenure_field.clear()
        tenure_field.send_keys(str(length_of_cd))

        time.sleep(1)

        # Handle the compounding dropdown
        compounding_dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@id='mat-select-0']"))
        )
        compounding_dropdown.click()

        compounding_option = wait.until(
            EC.presence_of_element_located((By.XPATH, f"//mat-option/span[contains(text(), '{compounding}')]"))
        )
        compounding_option.click()

        time.sleep(2)

        # Click the calculate button
        calculate_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='CIT-chart-submit']"))
        )
        calculate_button.click()

        # Wait for results to load
        time.sleep(5)

        # Print the result
        result_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='output']//span[@id='results-value']"))
        )
        print(f"Calculated Result: {result_element.text}")

    except Exception as e:
        print(f"Error encountered for row {row}: {e}")
        driver.save_screenshot(f"error_{row[0]}.png")  # Save a screenshot for debugging

driver.quit()
cursor.close()
db_connection.close()