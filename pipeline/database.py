"""Database setup for the weather pipeline"""

import sqlite3

DB_PATH = "data/weather.db"


def init_db():
    """Create weather table if it doesn't exist"""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()
