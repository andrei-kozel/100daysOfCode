import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]

sheety_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = self.get_data()

    def print_data(self):
        pprint(self.data)

    def get_data(self):
        self.data = requests.get(f"{sheety_endpoint}/flightDeals/prices").json()
        return self.data["prices"]

    def update_sheet(self, new_data):
        for data in new_data:
            new_data = {
                "price": data
            }
            response = requests.put(f"{sheety_endpoint}/flightDeals/prices/{data['id']}", json=new_data)
            response.raise_for_status()

        return self.get_data()

