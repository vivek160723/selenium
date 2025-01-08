from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def demo_cookie_methods(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        # Add a cookie
        driver.add_cookie({"name": "test_cookie", "value": "test_value"})

        # Retrieve a specific cookie
        cookie = driver.get_cookie("test_cookie")
        print("Retrieved Cookie:", cookie)

        # Retrieve all cookies
        cookies = driver.get_cookies()
        print("All Cookies:", cookies)

        # Delete a specific cookie
        driver.delete_cookie("test_cookie")
        print("Cookie Deleted.")

        # Delete all cookies
        driver.delete_all_cookies()
        print("All Cookies Deleted.")

    finally:
        driver.quit()


demo_cookie_methods("https://www.google.com/")