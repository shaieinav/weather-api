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

        weather_cols_data_type = {
            'longitude': Float(),
            'latitude': Float(),
            'forecast_time': String() if using_sqlite else DateTime(),
            'temperature': Float(),
            'precipitation': Float(),
        }

        weather_summary_cols_data_type = {
            'longitude': Float(),
            'latitude': Float(),
            'max_temperature': Float(),
            'min_temperature': Float(),
            'avg_temperature': Float(),
            'max_precipitation': Float(),
            'min_precipitation': Float(),
            'avg_precipitation': Float(),
        }

        dataframes = [pd.read_csv(file) for file in csv_files]
        engine = create_engine(db_uri)
        weather_df = pd.concat(dataframes)

        if not using_sqlite:
            weather_df['forecast_time'] = weather_df['forecast_time'].astype('datetime')

        weather_summary_df = weather_df.groupby(['longitude', 'latitude']).agg({'temperature': ['max', 'min', 'mean'], 'precipitation': ['max', 'min', 'mean']})
        weather_summary_df.columns = ['max_temperature', 'min_temperature', 'avg_temperature', 'max_precipitation', 'min_precipitation', 'avg_precipitation']
        weather_summary_df = weather_summary_df.reset_index()

        weather_df.to_sql(
            'weather',
            con=engine,
            if_exists='replace',
            index=False,
            chunksize=1000,
            dtype=weather_cols_data_type,
        )

        weather_summary_df.to_sql(
            'weather_summary',
            con=engine,
            if_exists='replace',
            index=False,
            chunksize=1000,
            dtype=weather_summary_cols_data_type,
        )

    except Exception as ex:
        return {'message': EXCEPTION_LOADING_DATA_TO_DB, 'Error': ex}
