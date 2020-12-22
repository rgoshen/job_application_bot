from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_EMAIL = "rick.goshen@gmail.com"
ACCOUNT_PASSWORD = "password"

chrome_driver_path = "/home/rgoshen/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(2)

# sign in
username_input = driver.find_element_by_id("username")
username_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element_by_id("password")
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)
