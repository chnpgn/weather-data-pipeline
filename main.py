"""The main execution module"""

from pipeline.extract import extract_weather
from pipeline.transform import transform_weather
from pipeline.load import load_weather
from pipeline.database import init_db


def run_pipeline():
    """The main execution function"""

    init_db()

    raw = extract_weather()

    transformed = transform_weather(raw)

    load_weather(transformed)

    print("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()
