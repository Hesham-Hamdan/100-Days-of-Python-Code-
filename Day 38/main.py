import os

from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]

API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
