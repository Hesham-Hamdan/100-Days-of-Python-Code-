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

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

