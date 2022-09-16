import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USER_TOKEN = os.environ["USER_TOKEN"]
PIXELA_USERNAME = os.environ["PIXELA_USERNAME"]

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USER_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create user
# response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "p",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

# create graph
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/graph1"
date_today = datetime.today().strftime('%Y%m%d')

pixel_config = {
    "date": date_today,
    "quantity": "100",
}

response = requests.post(pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)
