from db import db
from typing import Dict, List, Union

WeatherJSON = Dict[str, Union[float, str]]


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
            return {"message": ex.message}

    @classmethod
    def find_by_longitude_and_latitude_and_forecast_time(
        cls, longitude, latitude, forecast_time
    ) -> "WeatherDataModel":

        return cls.query.filter_by(
            longitude=longitude, latitude=latitude, forecast_time=forecast_time
        ).one_or_none()

    @classmethod
    def find_max_min_avg(cls, longitude, latitude):
        pass

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
