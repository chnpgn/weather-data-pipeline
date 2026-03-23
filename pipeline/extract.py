"""Extract weather data from the OpenWeather API"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY", "Johannesburg")

URL = "https://api.openweathermap.org/data/2.5/weather"


def extract_weather():
    """Fetch weather data from the API"""

    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()
