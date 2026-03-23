"""Main pipeline runner"""

from pipeline.extract import extract_weather
from pipeline.transform import transform_weather
from pipeline.load import load_weather


def run_pipeline():
    """Execute the ETL pipeline"""

    raw_data = extract_weather()

    transformed_data = transform_weather(raw_data)

    load_weather(transformed_data)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
