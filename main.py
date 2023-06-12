import requests
from datetime import datetime
import os

NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]

GENDER = {GENDER}  # male/female
WEIGHT_KG = {WEIGHT}
HEIGHT_CM = {HEIGHT}
AGE = {AGE}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_query = input("What exercise(s) did you do? ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)

data = response.json()['exercises']

today = datetime.now()
date = today.strftime("%m/%d/%Y")
time = today.strftime("%H:%M:%S")

headers = {
    "Authorization": SHEETY_AUTH
}

for exercise in data:
    row = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=row, headers=headers)
