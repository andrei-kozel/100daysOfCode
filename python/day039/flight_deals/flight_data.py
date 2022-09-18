import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
tequila_endpoint = "https://api.tequila.kiwi.com/v2"
tequila_headers = {
    "apikey": TEQUILA_API_KEY
}


class FlightData:
    def get_flight_data(self, code):
        config = {
            "fly_from": "GOT",
            "fly_to": code,
            "date_from": (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y'),
            "date_to": (datetime.date.today() + datetime.timedelta(days=180)).strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0
        }
        response = requests.get(f"{tequila_endpoint}/search", params=config, headers=tequila_headers)
        if response.json()["data"]:
            return f"{response.json()['data'][0]['price']} EUR"
        else:
            return "No flights"
