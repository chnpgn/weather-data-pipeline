"""The main execution module"""

import time
import schedule

from pipeline.extract import extract_weather
from pipeline.transform import transform_weather
from pipeline.load import load_weather
from pipeline.database import init_db


def run_pipeline():
    """"The main function """
    raw = extract_weather()
    transformed = transform_weather(raw)
    load_weather(transformed)

init_db()

schedule.every(1).hours.do(run_pipeline)
print("Pipeline scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)
