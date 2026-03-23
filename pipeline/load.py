# """Load processed data into storage"""

# import json
# import os


# def load_weather(data: dict, filename="data/weather_data.json"):
#     """Save processed weather data"""

#     os.makedirs("data", exist_ok=True)

#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(data, file, indent=4)

#     print("Data successfully saved")


"""Load transformed weather data into database"""

import sqlite3

DB_PATH = "data/weather.db"


def load_weather(data: dict):
    """Loads weather data to database function"""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO weather (city, temperature, humidity, pressure, weather, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            data["city"],
            data["temperature"],
            data["humidity"],
            data["pressure"],
            data["weather"],
            data["timestamp"],
        ),
    )

    conn.commit()
    conn.close()

    print("Data inserted into database")
