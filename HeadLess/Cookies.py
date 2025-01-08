from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def add_cookies_to_browser(url, cookies):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        return driver.get_cookies()
    finally:
        driver.quit()


url = "https://www.google.com/"
cookies_to_add = [
    {"name": "test_cookie", "value": "test_value"},
    {"name": "example_cookie", "value": "example_value"}
]

added_cookies = add_cookies_to_browser(url, cookies_to_add)
print("Added Cookies:", added_cookies)