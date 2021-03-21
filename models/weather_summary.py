#from os import environ

from db import db

#using_sqlite = environ.get('DATABASE_URL', 'sqlite:///test.db') == 'sqlite:///test.db'
#FORECAST_TIME_COLUMN_TYPE = db.String if using_sqlite else db.DateTime
EXCEPTION_FETCHING_FROM_DB = 'Exception while trying to get weather summary '\
                             'data from the database.'


class WeatherSummaryModel(db.Model):

    __tablename__ = 'weather_summary'
    longitude = db.Column(db.Float(precision=1))
    latitude = db.Column(db.Float(precision=1))
    #forecast_time = db.Column(FORECAST_TIME_COLUMN_TYPE)
    min_temperature = db.Column(db.Float(precision=1), nullable=False)
    max_temperature = db.Column(db.Float(precision=1), nullable=False)
    min_precipitation = db.Column(db.Float(precision=1), nullable=False)
    max_precipitation = db.Column(db.Float(precision=1), nullable=False)
    avg_temperature = db.Column(db.Float(precision=2), nullable=False)
    avg_precipitation = db.Column(db.Float(precision=2), nullable=False)

    #weather_data = db.relationship('WeatherDataModel')

    __table_args__ = (
        db.PrimaryKeyConstraint(
            'longitude',
            'latitude',
        ),
        #db.ForeignKeyConstraint(
            #['longitude', 'latitude'],
            #['longitude', 'latitude', 'forecast_time'],
            #['weather.longitude', 'weather.latitude']
            #['weather.longitude', 'weather.latitude', 'weather.forecast_time']
        #),
        #db.UniqueConstraint(
            #'longitude',
            #'latitude',
            #'forecast_time'
        #),
    )

    @classmethod
    def find_by_longitude_and_latitude(
        cls, longitude, latitude
    ) -> 'WeatherSummaryModel':
        try:
            return cls.query.filter_by(longitude=longitude, latitude=latitude).first()
        except Exception as ex:
            return {'message': EXCEPTION_FETCHING_FROM_DB, 'Error': ex}
