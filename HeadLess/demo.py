from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_title(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        return driver.title
    finally:
        driver.quit()

url = "https://www.google.com/"
page_title = get_page_title(url)
print("Page Title:", page_title)