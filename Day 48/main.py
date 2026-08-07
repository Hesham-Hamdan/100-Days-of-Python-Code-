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

times = []
events = []
for li in lis:
    times.append(
        li.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    )
    events.append(li.find_element(By.TAG_NAME, "a").text)

result = {
    index: {"time": times[index], "name": events[index]}
    for index in range(0, len(times))
}

print(result)
driver.quit()
