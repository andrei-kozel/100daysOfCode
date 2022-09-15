import requests
import os
from datetime import date
from datetime import timedelta
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# .env
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']

stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'
r = requests.get(stock_url)
data = r.json()
yesterday = date.today() - timedelta(days=1)
day_before_yesterday = date.today() - timedelta(days=2)

yesterday_price = data["Time Series (Daily)"][f'{yesterday}']['4. close']
day_before_yesterday_price = data["Time Series (Daily)"][f'{day_before_yesterday}']['4. close']

difference = float(yesterday_price) - float(day_before_yesterday_price)
diff_percent = (difference / float(yesterday_price)) * 100

up_down = ""
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff_percent > 5:
    news_url = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "from": day_before_yesterday_price,
        "apiKey": NEWS_API_KEY,
        "sortBy": "popularity"
    }
    news_response = requests.get(news_url, params=news_parameters)
    news_data = news_response.json()['articles'][:3]

    formatted_articles = [f"TSLA: {up_down}{diff_percent}% \nHeadline: {news['title']}. \nBrief: {news['description']}"
                          for news in news_data]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(body=article,
                                         from_=os.environ['TWILIO_PHONE_NUMBER'],
                                         to=os.environ['PHONE_NUMBER'])
