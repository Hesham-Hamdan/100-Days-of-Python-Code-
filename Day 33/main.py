import requests


iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_data = iss_response.json()


longitude = float(iss_data["iss_position"]["longitude"])
latitude = float(iss_data["iss_position"]["latitude"])
