from db import db
from typing import List


class WeatherDataModel(db.Model):

    __tablename__ = "weather"
    longitude = db.Column(db.Float(precision=1))
    latitude = db.Column(db.Float(precision=1))
    forecast_time = db.Column(db.DateTime)
    temperature = db.Column(db.Float(precision=1), nullable=False)
    precipitation = db.Column(db.Float(precision=1), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(
            "longitude",
            "latitude",
            "forecast_time",
        ),
    )

    @classmethod
    def find_by_longitude_and_latitude(
        cls, longitude, latitude
    ) -> List["WeatherDataModel"]:
        try:
            return cls.query.filter_by(longitude=longitude, latitude=latitude).all()
        except Exception as ex:
            return {"Exception while trying to get weather data from the database.": ex}
