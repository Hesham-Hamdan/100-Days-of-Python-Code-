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

response = requests.post(url=pixela_endpoint, json=users_params)
print(response.text)

