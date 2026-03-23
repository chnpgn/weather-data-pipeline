import sqlite3
import pandas as pd

conn = sqlite3.connect("data/weather.db")
df = pd.read_sql_query("SELECT * FROM weather", conn)
print(df.describe())
print("\nAverage temperature:", df["temperature"].mean())
