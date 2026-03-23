"""The data generator module"""

import sqlite3
import random
from datetime import datetime, timedelta


def generate_weather_data(num_records=20):
    """The data generator function"""
    cities = ["New York", "London", "Tokyo",
              "Paris", "Berlin", "Sydney", "Dubai"]
    conditions = ["Clear", "Clouds", "Rain", "Thunderstorm", "Snow", "Mist"]

    data = []
    start_time = datetime.now()

    for i in range(num_records):
        city = random.choice(cities)
        # Random temperature between -10 and 35°C
        temp = round(random.uniform(-10.0, 35.0), 1)
        # Humidity between 30% and 90%
        humidity = random.randint(30, 90)
        # Pressure around 1013 hPa
        pressure = random.randint(1000, 1025)
        weather = random.choice(conditions)
        # Create timestamps at 1-hour intervals moving backward
        timestamp = (start_time - timedelta(hours=i)
                     ).strftime("%Y-%m-%d %H:%M:%S")

        # This tuple matches your (?, ?, ?, ?, ?, ?) structure
        data.append((city, temp, humidity, pressure, weather, timestamp))

    return data


# --- Database Execution ---
DB_PATH = "data/weather_data.db"
sample_data = generate_weather_data(50)

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            pressure INTEGER,
            weather TEXT,
            timestamp TEXT
        )
    """)

    # Use executemany for high-speed bulk insertion
    QUERY = "INSERT INTO weather (city, temperature, humidity, pressure, weather, timestamp) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.executemany(QUERY, sample_data)

    conn.commit()
    print(f"Successfully inserted {len(sample_data)} rows into {DB_PATH}.")
