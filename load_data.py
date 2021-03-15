from pandas import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Float, DateTime, String

EXCEPTION_LOADING_DATA_TO_DB = 'Exception while trying to load data from'\
                               'pandas to postgresql database'


def load_csv_data(db_uri):

    using_sqlite = db_uri == 'sqlite:///test.db'

    try:
        if using_sqlite:
            csv_files = [f'csv_weather_data/file{file_num}.csv'
                         for file_num in range(1, 4)]
        else:
            csv_files = [f'/var/www/html/weather-api/csv_weather_data/file{file_num}.csv'
                         for file_num in range(1, 4)]

        cols_data_type = {
            'longitude': Float(),
            'latitude': Float(),
            'forecast_time': String() if using_sqlite else DateTime(),
            'temperature': Float(),
            'precipitation': Float(),
        }

        dataframes = [pd.read_csv(file) for file in csv_files]
        engine = create_engine(db_uri)
        weather_df = pd.concat(dataframes)

        if not using_sqlite:
            weather_df['forecast_time'] = weather_df['forecast_time'].astype('datetime')

        weather_df.to_sql(
            'weather',
            con=engine,
            if_exists='replace',
            index=False,
            chunksize=1000,
            dtype=cols_data_type,
        )

    except Exception as ex:
        return {'message': EXCEPTION_LOADING_DATA_TO_DB, 'Error': ex}
