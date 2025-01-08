import time
import openpyxl
from openpyxl.styles import PatternFill
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Define Excel functions
def getRowCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_row

def getColumnCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_column

def readData(file, sheetName, rownum, columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(rownum, columnno).value

def writeData(file, sheetName, rownum, columnno, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    sheet.cell(rownum, columnno).value = data
    workbook.save(file)

def fillGreenColor(file, sheetName, rownum, columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    greenFill = PatternFill(start_color='60b212',
                            end_color='60b212',
                            fill_type='solid')

    sheet.cell(rownum, columnno).fill = greenFill
    workbook.save(file)

def fillRedColor(file, sheetName, rownum, columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    redFill = PatternFill(start_color='ff0000',
                          end_color='ff0000',
                          fill_type='solid')
    sheet.cell(rownum, columnno).fill = redFill
    workbook.save(file)

# Excel File and Sheet Details
file = '/Users/vivekkumar/Downloads/simple_interest_data.xlsx'
sheetName = 'Sheet1'

# Read values from the Excel file
deposit_amount = readData(file, sheetName, 2, 1)
tenure = readData(file, sheetName, 2, 2)
interest_rate = readData(file, sheetName, 2, 3)

# Set up Chrome options and driver
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

# Wait for the form elements to be visible
wait = WebDriverWait(driver, 20)
deposit_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='principal']")))
deposit_field.clear()
deposit_field.send_keys(str(deposit_amount))

rate_field = driver.find_element(By.ID, "interest")
rate_field.clear()
rate_field.send_keys(str(interest_rate))

tenure_field = driver.find_element(By.ID, "tenure")
tenure_field.clear()
tenure_field.send_keys(str(tenure))

# Wait for the overlay to become invisible
try:
    overlay = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "wzrk-overlay")))
except:
    print("Overlay did not disappear in time, proceeding...")

# Find the calculate button and click it
calculate_button = driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img")
action = ActionChains(driver)
action.move_to_element(calculate_button).click().perform()

# Wait for the maturity amount field to be visible
wait.until(EC.visibility_of_element_located((By.ID, "maturityAmt")))

# Retrieve and store the result
result = driver.find_element(By.ID, "maturityAmt").text
writeData(file, sheetName, 2, 4, result)

# Apply color based on result (Example: If result is high, fill green, else red)
if float(result) > 50000:  # Adjust your condition
    fillGreenColor(file, sheetName, 2, 4)
else:
    fillRedColor(file, sheetName, 2, 4)

# Close the browser
driver.quit()