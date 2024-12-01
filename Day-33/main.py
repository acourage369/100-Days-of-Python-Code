import smtplib
import time
from http.client import responses

import requests
from datetime import datetime

MY_LAT = 5.651955
MY_LONG = -0.187107
MY_EMAIL = "acourage009@gmail.com"
MY_PASSWORD = "xpuwtllspiwerqml"

# Error codes
# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go away
# 4XX: You screwed up
# 5XX: I screwed up

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


def is_iss_overhead():
    response = requests.get(url="https://api.sunrise-sunset.org/json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    iss_longitude = float(data["results"]["sunset"].split("T")[1].split(":")[0])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now<= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up☝️\n\nThe ISS is above you in the sky."
        )




