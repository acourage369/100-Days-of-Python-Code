import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os

# Load environment variables from a .env file
load_dotenv()

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OPENWEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 4.710989,
    "lon": -74.072090,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url=api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain =False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella☔",
        from_= os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("RECIPIENT_PHONE_NUMBER"),
    )

    print(message.status)

