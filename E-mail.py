# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# # Sender's email credentials
# sender_email = "chaudharyvivek250103@gmail.com"  # Replace with your email address
# app_password = "pnzlxfcupryrnoka"       # Replace with the App Password generated in Step 2
#
# # Recipient's email address
# recipient_email = "gauravmaan0009@gmail.com"  # Replace with your friend's email address
#
# # Email subject and body
# subject = "Hello, Friend!"
# body = "Hi, this is a test email from my Python script. How are you?"
#
# # Create the email
# email = MIMEMultipart()
# email["From"] = sender_email
# email["To"] = recipient_email
# email["Subject"] = subject
# email.attach(MIMEText(body, "plain"))
#
# # Send the email
# try:
#     print("Connecting to SMTP server...")
#     # Connect to the SMTP server
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Using Gmail's SMTP server
#         server.starttls()  # Upgrade to secure connection
#         print("Login attempt...")
#         server.login(sender_email, app_password)  # Login with App Password
#         print("Sending email...")
#         server.sendmail(sender_email, recipient_email, email.as_string())  # Send the email
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (Change 'Chrome' to 'Safari' if using Safari)
driver = webdriver.Safari()

# Open Gmail
driver.get("https://mail.google.com")

# Wait for the page to load
time.sleep(2)

# Enter your email
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("chaudharyvivek250103@gmail.com")  # Replace with your Gmail email address
email_field.send_keys(Keys.RETURN)  # Press Enter to proceed to the next step

# Wait for the password page to load
time.sleep(2)

# Enter your password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("pnzlxfcupryrnoka")  # Replace with your Gmail password
password_field.send_keys(Keys.RETURN)  # Press Enter to log in

# Wait for a while to see the result
time.sleep(5)

# Close the browser
driver.quit()
