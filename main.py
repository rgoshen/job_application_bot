from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_EMAIL = "rick.goshen@gmail.com"
ACCOUNT_PASSWORD = "NitL10n$#1"
PHONE = "520-639-0031"

chrome_driver_path = "/home/rgoshen/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(2)

# sign in
username_input = driver.find_element_by_id("username")
username_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element_by_id("password")
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)

# Locate the apply button
time.sleep(2)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(2)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

# Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
