import time
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


# step 7

days = ["tue", "thu"]
new_bookings = []
new_waitlists = []

already_booked = 0
already_joined = 0
classes_booked = 0
wailists_joined = 0


def verify_bookings(num_of_bookings, container_divs_id):
    if num_of_bookings > 0:
        my_bookings_button = driver.find_element(By.ID, "my-bookings-link")
        my_bookings_button.click()
        container_divs = driver.find_element(By.ID, container_divs_id).find_elements(
            By.CSS_SELECTOR, "div [id*='card']"
        )
        print("--- VERIFYING ON MY BOOKINGS PAGE ---")

        for div in container_divs:
            class_type = div.find_element(By.CSS_SELECTOR, "div h3").text
            # class_time = div.find_element(By.CSS_SELECTOR, "div p").text
            print(f"✓ Verified: {class_type}")
        print("--- VERIFICATION RESULT ---")
        print(f"Expected: {num_of_bookings} bookings")
        print(f"Found: {len(container_divs)} bookings")
        if num_of_bookings == len(container_divs):
            print("✅ SUCCESS: All bookings verified!")
        else:
            print(
                f"❌ MISMATCH: Missing {num_of_bookings - len(container_divs)} bookings"
            )


for day in days:
    time.sleep(1)
    div_parent = driver.find_element(By.CSS_SELECTOR, f"[id*='{day}']")
    h2 = div_parent.find_element(By.CSS_SELECTOR, "h2").text
    div_wrapper = div_parent.find_element(By.CSS_SELECTOR, "[id$='-1800']")
    class_type = div_wrapper.find_element(By.CSS_SELECTOR, "h3").text
    book_button = div_wrapper.find_element(By.TAG_NAME, "button")

    if book_button.text == "Booked":
        print(f"✓ Already booked: {class_type} on {h2}")
        already_booked += 1
    elif book_button.text == "Waitlisted":
        print(f"✓ Already on waitlist: {class_type} on {h2}")
        already_joined += 1
    else:
        try:
            book_button.click()
            time.sleep(1)
        except Exception:
            driver.execute_script("arguments[0].click();", book_button)
            time.sleep(1)
        finally:
            if book_button.text == "Booked":
                print(f"✓ Booked: {class_type} on {h2}")
                classes_booked += 1
                new_bookings.append(f"{class_type} on {h2}")
            else:
                print(f"✓ Joined waitlist for: {class_type} on {h2}")
                wailists_joined += 1
                new_waitlists.append(f"{class_type} on {h2}")


print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {classes_booked}")
print(f"Waitlists joined: {wailists_joined}")
print(f"Already booked/waitlisted: {already_booked+already_joined}")
print(
    f"Total Tuesday & Thursday 6pm classes processed: {classes_booked + wailists_joined +already_booked+already_joined}"
)


verify_bookings(classes_booked + already_booked, "confirmed-bookings-section")
verify_bookings(wailists_joined + already_joined, "waitlist-section")
