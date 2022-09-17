import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

user_input = input("Tell me which exercises you did: ")

NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID']
NUTRITIONIX_APP_KEY = os.environ['NUTRITIONIX_APP_KEY']
SHEETY_API_KEY = os.environ['SHEETY_API_KEY']

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}
nutritionix_data = {
    "query": user_input
}

nutritionix_response = requests.post(nutritionix_endpoint, json=nutritionix_data, headers=nutritionix_headers)
exercises = nutritionix_response.json()['exercises']

for exercise in exercises:
    sheety_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutTracking/workouts"

    sheety_data = {
        "workout": {
            "date": datetime.today().strftime('%d/%m/%Y'),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise['name'].capitalize(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    requests.post(sheety_endpoint, json=sheety_data)
