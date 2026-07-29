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

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


if difference_precentage <= -5 or difference_precentage >= 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "from": "2026-06-31",
        "sortBy": "publishedAt",
        "apiKey": "afa580b6630f491d833e03fb936a5f94",
    }
    news_response = requests.get(NEWS_API, params=news_parameters)
    news_data = news_response.json()
    news_pieces = [news_data["articles"][num] for num in range(0, 3)]
    if difference_precentage > 0:
        body = f"🔺{round(difference_precentage)}"
    elif difference_precentage < 0:
        body = f"🔺{round(-difference_precentage)}"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: {body}%\nHeadline: {news_pieces[0]['title']}\nBrief: {news_pieces[0]['description']}",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER",
    )
    print(message.status)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
