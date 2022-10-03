import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 13.067439  # Your latitude
MY_LONG = 80.237617  # Your longitude

MY_EMAIL = "kumrev2003@gmail.com"
MY_PASSWORD = "revathi2019"
time_now = datetime.now()
current_hour = time_now.hour
current_second = time_now.second


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    global current_hour
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if current_hour >= sunset or current_hour <= sunrise:
        return True


# If the ISS is close to my current position
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(" smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="subject:Look up!!\n\nThe ISS is above you in the sky")
            connection.close()
