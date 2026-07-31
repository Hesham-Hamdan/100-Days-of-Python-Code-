from datetime import datetime
import requests


TOKEN = "kdlfgjkfdjgfdjldsf"
USERMAME = "hesham999"
GRAPH_ID = "graph0"
pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username": USERMAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERMAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Food Graph",
    "unit": "calory",
    "type": "float",
    "color": "sora",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2026, month=7, day=5)

pixel_config = {"date": today.strftime("%Y%m%d"), "quantity": "1550"}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

updating_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

updating_pixel_config = {"quantity": "1250"}

# response = requests.put(
#     url=updating_pixel_endpoint, json=updating_pixel_config, headers=headers
# )
# print(response.text)


response = requests.delete(url=updating_pixel_endpoint, headers=headers)
print(response.text)
