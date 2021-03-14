from pandas import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Float, DateTime


def load_csv_data(db_uri):
   
    try:
        csv_files = [
            "/var/www/html/weather-api/csv_weather_data/file1.csv",
            "/var/www/html/weather-api/csv_weather_data/file2.csv",
            "/var/www/html/weather-api/csv_weather_data/file3.csv",
        ]

        cols_data_type = {
            "longitude": Float(),
            "latitude": Float(),
            "forecast_time": DateTime(),
            "temperature": Float(),
            "precipitation": Float()
        }

        dataframes = [pd.read_csv(file) for file in csv_files]
        engine = create_engine(db_uri)
        weather_df = pd.concat(dataframes)
        weather_df['forecast_time'] = weather_df['forecast_time'].astype('datetime')
        weather_df.to_sql('weather', con=engine, if_exists='replace', index=False, chunksize = 1000, dtype=cols_data_type)

    except Exception as ex:
        return {"Exception while trying to load data from pandas to postgresql database": ex}
