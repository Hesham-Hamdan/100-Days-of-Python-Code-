import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "afa580b6630f491d833e03fb936a5f94"
STOCK_API_KEY = "J16XZTTXL3N4VP2R"

NEWS_API = "https://newsapi.org/v2/everything"
STOCK_PRICE_API = "https://www.alphavantage.co/query"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_PRICE_API, params=stock_parameters)
stock_data = stock_response.json()
data_list = list(stock_data["Time Series (Daily)"].values())

yesterday_price = float(data_list[0]["4. close"])
theday_before_price = float(data_list[1]["4. close"])

difference_precentage = (yesterday_price - theday_before_price) / yesterday_price * 100

print(difference_precentage)

