from datetime import datetime
import requests


iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_data = iss_response.json()


longitude = float(iss_data["iss_position"]["longitude"])
latitude = float(iss_data["iss_position"]["latitude"])


MY_LAT = 30.725775
MY_LONG = 31.798065

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunset)
print(sunrise)

time_now = datetime.now()
# print(time_now.hour)


def check_position(lat, lng):
    if abs(lat - MY_LAT) <= 5 and abs(lng - MY_LONG) <= 5:
        return True
    else:
        return False


if check_position(latitude, longitude) and (
    time_now.hour > sunset or time_now.hour < sunrise
):
    print("it's here")
else:
    print("Oh no it's far from here")
