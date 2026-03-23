"""Transform raw weather API data"""

from datetime import datetime


def transform_weather(data: dict):
    """Clean and structure weather data"""

    transformed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "timestamp": datetime.utcnow().isoformat()
    }

    return transformed
