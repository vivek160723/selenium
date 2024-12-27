# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
#
# try:
#     driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
#
#     frame1 = driver.find_element(By.XPATH, "//*[@id='frm1']")
#     driver.switch_to.frame(frame1)
#
#     dropdown_element = driver.find_element(By.XPATH, "//*[@id='course']")
#     dropdown = Select(dropdown_element)
#     print("Available options:")
#     for option in dropdown.options:
#         print(option.text)
#
#     dropdown.select_by_visible_text("Java")
#     print("Selected 'Java'")
#     time.sleep(5)
#
#     driver.switch_to.default_content()
#
# finally:
#     driver.quit()
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
#
# try:
#     driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
#
#     frame1 = driver.find_element(By.XPATH, "//*[@id='frm1']")
#     driver.switch_to.frame(frame1)
#
#     dropdown_element = driver.find_element(By.XPATH, "//*[@id='selectnav1']")
#     dropdown = Select(dropdown_element)
#     print("Available options:")
#     for option in dropdown.options:
#         print(option.text)
#
#     # dropdown.select_by_visible_text("Java")
#     # print("Selected 'Java'")
#     time.sleep(5)
#
#     driver.switch_to.default_content()
#
# finally:
#     driver.quit()