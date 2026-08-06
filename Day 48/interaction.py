from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num = driver.find_element(By.ID, "mwDw").text
# print(num)
driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME, "fName")
firstname.send_keys("hesham")
lastname = driver.find_element(By.NAME, "lName")
lastname.send_keys("hamdan")
email = driver.find_element(By.NAME, "email")
email.send_keys("fdsfsd@gmail.com", Keys.ENTER)

# button = driver.find_element(By.CSS_SELECTOR, "button")
# button.click()

driver.quit()
