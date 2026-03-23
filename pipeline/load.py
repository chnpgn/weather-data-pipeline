"""Load processed data into storage"""

import json
import os


def load_weather(data: dict, filename="data/weather_data.json"):
    """Save processed weather data"""

    os.makedirs("data", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Data successfully saved")
