import os
import requests
from dotenv import load_dotenv

load_dotenv()

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
tequila_endpoint = "https://api.tequila.kiwi.com"
tequila_headers = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    @staticmethod
    def get_destination_code(city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(f"{tequila_endpoint}/locations/query", params=query, headers=tequila_headers)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]

        return code
