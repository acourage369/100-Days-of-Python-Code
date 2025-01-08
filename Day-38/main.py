import os
from datetime import datetime
import requests

GENDER = "male"
WEIGHT_KG = 45
HEIGHT_CM = 5
AGE = 22

APP_ID = os.environ["APP_ID"] #raises exception if key does not exist
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
TOKEN = os.environ.get("TOKEN")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = "https://api.sheety.co/acaa93349d3e57287898820f98b5a5c6/myWorkouts(brainy)/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
    }
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
