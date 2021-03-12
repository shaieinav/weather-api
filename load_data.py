from pandas import pandas as pd
from sqlalchemy import create_engine


def load_csv_data(db_uri):
    csv_files = [
        "csv_weather_data/file1.csv",
        "csv_weather_data/file2.csv",
        "csv_weather_data/file3.csv",
    ]

    dataframes = [pd.read_csv(file) for file in csv_files]
    engine = create_engine(db_uri)
    weather_df = pd.concat(dataframes)
    weather_df.to_sql("weather", engine, if_exists="replace", index=False)
