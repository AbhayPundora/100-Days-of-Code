import requests
import datetime as dt
from twilio.rest import Client
import time

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid ="AC209d36747005271ecdcdcjvfndv"
auth_token="9ee2efbf30dvjfdnkcsdcks84664fac061"


today = dt.datetime.now().today()
y_date = (today - dt.timedelta(days=3)).date()
p_date = (today - dt.timedelta(days=4)).date()
print(today)
print(y_date)
print(p_date)

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=M6QCVXMDUBDCKJBDY1BQ")
print(response.json())
yesterday_closing_price = float(response.json()["Time Series (Daily)"][str(y_date)]['4. close'])
day_before_yesterday_closing_price = float(response.json()["Time Series (Daily)"][str(p_date)]['4. close'])

print(yesterday_closing_price)
print(day_before_yesterday_closing_price)

diff = yesterday_closing_price - day_before_yesterday_closing_price
profit_or_lose  = ( diff * 100 ) / yesterday_closing_price

print(diff)
print(profit_or_lose)

if profit_or_lose > 0:
    sign = "🔺"
else:
    sign = "🔻"


if abs(profit_or_lose) >= 5:
    news_articles = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from={str(y_date)}&to={str(y_date)}&sortBy=popularity&page=3&apiKey=baa6a0b7d4ae44e4addbcbksdc4da9fbe")
    print(news_articles.json())
    data = news_articles.json()
    title = [item["title"] for item in data["articles"]][0:3]
    print(title)
    description = [item["description"] for item in data["articles"]][0:3]
    print(description)

    client = Client(account_sid, auth_token)

    for i in range(0, 3):
        time.sleep(2)
        message = client.messages.create(
            to="+9190274898815",
            from_="+18623782981",
            body=f"{STOCK}: {sign}{round(abs(profit_or_lose))}% \nHeadline: {title[i]} ({STOCK})?. Brief:{description[i]}")

        print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

