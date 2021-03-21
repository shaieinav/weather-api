from db import db

EXCEPTION_FETCHING_FROM_DB = 'Exception while trying to get weather summary '\
                             'data from the database.'


class WeatherSummaryModel(db.Model):

    __tablename__ = 'weather_summary'
    longitude = db.Column(db.Float(precision=1))
    latitude = db.Column(db.Float(precision=1))
    min_temperature = db.Column(db.Float(precision=1), nullable=False)
    max_temperature = db.Column(db.Float(precision=1), nullable=False)
    min_precipitation = db.Column(db.Float(precision=1), nullable=False)
    max_precipitation = db.Column(db.Float(precision=1), nullable=False)
    avg_temperature = db.Column(db.Float(precision=2), nullable=False)
    avg_precipitation = db.Column(db.Float(precision=2), nullable=False)

    weather_data = db.relationship('WeatherDataModel')

    __table_args__ = (
        db.PrimaryKeyConstraint(
            'longitude',
            'latitude',
        ),
        db.ForeignKeyConstraint(
            ['longitude', 'latitude'],
            ['weather.longitude', 'weather.latitude']
        ),
    )

    @classmethod
    def find_by_longitude_and_latitude(
        cls, longitude, latitude
    ) -> 'WeatherSummaryModel':
        try:
            return cls.query.filter_by(longitude=longitude, latitude=latitude).first()
        except Exception as ex:
            return {'message': EXCEPTION_FETCHING_FROM_DB, 'Error': ex}
