import requests
import os
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]

API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

params = {
    "query": input("Tell me which exercies you did: "),
    "weight_kg": 85,
    "height_cm": 170,
    "age": 26,
    "gender": "male",
}

headers = {"x-app-id": API_ID, "x-app-key": API_KEY}
