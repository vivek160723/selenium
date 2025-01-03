from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Set implicit wait
driver.implicitly_wait(10)

# Open Amazon
driver.get("https://www.amazon.com/")

# Perform a search query
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Laptop")
search_box.submit()

# Wait for search results to load
search_results = driver.find_element(By.XPATH, "//span[contains(text(),'results for')]")
print(search_results.text)

# Close the driver
driver.quit()

############## Explicit wait ##################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Amazon
driver.get("https://www.amazon.com/")

# Perform a search query
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Laptop")
search_box.submit()

# Wait explicitly for search results to load
wait = WebDriverWait(driver, 10)  # 10 seconds timeout
search_results = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'results for')]")))
print(search_results.text)

# Navigate back to home page to wait for product recommendations
driver.get("https://www.amazon.com/")

# Wait explicitly for product recommendations
recommendations = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-carousel")))
print("Product recommendations loaded.")

# Close the driver
driver.quit()
