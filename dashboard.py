import sqlite3
import streamlit as st
import pandas as pd

conn = sqlite3.connect("data/weather.db")

df = pd.read_sql_query("SELECT * FROM weather", conn)

st.title("Weather Data Dashboard")

st.write("Recent Weather Data")
st.dataframe(df)

st.line_chart(df["temperature"])
