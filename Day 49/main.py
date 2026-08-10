from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


ACCOUNT_EMAIL = "hossam@gmail.com"  # The email you registered with
ACCOUNT_PASSWORD = "hossam@gmail.com"  # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

# step 2

driver.implicitly_wait(2)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
email_field = driver.find_element(By.ID, "email-input")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password-input")
password_field.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)
