from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
)
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for the page to load
sleep(3)

# 1. DISMISS THE COOKIE CONSENT BANNER
try:
    # Locate the "Got it!" or "Accept All" button on the consent banner
    cookie_consent_btn = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
    cookie_consent_btn.click()
    print("Cookie consent banner dismissed successfully!")
    sleep(1)  # Short pause to let the banner slide away
except NoSuchElementException:
    # If the banner doesn't show up for some reason, just carry on
    print("No cookie consent banner detected, proceeding...")

# 2. SELECT LANGUAGE
lang = driver.find_element(By.ID, "langSelect-EN")
lang.click()

# Give the main game interface a moment to load
sleep(3)


def play():
    timeout = time() + 5

    while True:
        # 1. Try to click the big cookie
        try:
            big_cookie = driver.find_element(By.ID, "bigCookie")
            big_cookie.click()
        except StaleElementReferenceException:
            continue

        # 2. Every 5 seconds, check for affordable upgrades
        if time() > timeout:
            try:
                cookies_text = driver.find_element(By.ID, "cookies").text.split(" ")[0]
                cookies_num = int(cookies_text.replace(",", ""))

                products = driver.find_elements(By.CLASS_NAME, "product")

                for product in reversed(products):
                    price_element = product.find_element(By.CLASS_NAME, "price")
                    price_text = price_element.text.replace(",", "")

                    if price_text.isdigit():
                        price = int(price_text)
                        if cookies_num >= price:
                            product.click()
                            break  # Exit shop loop and go back to clicking

            except StaleElementReferenceException:
                pass

            # Reset the 5-second timer
            timeout = time() + 5


# Start the bot
play()
