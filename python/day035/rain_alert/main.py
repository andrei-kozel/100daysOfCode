import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

parameters = {
    "lat": 57.708870,
    "lon": 11.974560,
    "appid": os.environ['WEATHER_APP_ID'],
    "exclude": "minutely,daily,current"
}

# twilio setup
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data['hourly'][0:12]

will_rain = False

for weather in hourly_weather:
    weather_code = weather['weather'][0]['id']
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=os.environ['TWILIO_PHONE_NUMBER'],
        to=os.environ['PHONE_NUMBER']
    )
