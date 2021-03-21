from os import environ

from db import db
from typing import List

using_sqlite = environ.get('DATABASE_URL', 'sqlite:///test.db') == 'sqlite:///test.db'
FORECAST_TIME_COLUMN_TYPE = db.String if using_sqlite else db.DateTime
EXCEPTION_FETCHING_FROM_DB = 'Exception while trying to get weather data from'\
                             'the database.'


class WeatherDataModel(db.Model):

    __tablename__ = 'weather'
    longitude = db.Column(db.Float(precision=1))
    latitude = db.Column(db.Float(precision=1))
    forecast_time = db.Column(FORECAST_TIME_COLUMN_TYPE)
    temperature = db.Column(db.Float(precision=1), nullable=False)
    precipitation = db.Column(db.Float(precision=1), nullable=False)

    #weather_summary = db.relationship('WeatherSummaryModel')

    __table_args__ = (
        db.PrimaryKeyConstraint(
            'longitude',
            'latitude',
            'forecast_time',
        ),
        #db.UniqueConstraint(
            #'longitude',
            #'latitude',
            #'forecast_time'
        #),
    )

    @classmethod
    def find_by_longitude_and_latitude(
        cls, longitude, latitude
    ) -> List['WeatherDataModel']:
        try:
            return cls.query.filter_by(longitude=longitude, latitude=latitude).all()
        except Exception as ex:
            return {'message': EXCEPTION_FETCHING_FROM_DB, 'Error': ex}
