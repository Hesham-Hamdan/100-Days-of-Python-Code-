from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

lis = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
).find_elements(By.TAG_NAME, "li")
