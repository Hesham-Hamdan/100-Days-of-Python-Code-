from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
price = f'{soup.select_one(".a-price-whole").getText()}{soup.select_one(".a-price-fraction").getText()}'
print(price)
