from ma import ma
from models.weather_data import WeatherDataModel


class WeatherDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeatherDataModel
        load_only = (
            'longitude',
            'latitude',
        )
        load_instance = True
