from ma import ma
from models.weather_data import WeatherDataModel
from models.weather_summary import WeatherSummaryModel


class WeatherDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeatherDataModel
        load_only = (
            'longitude',
            'latitude',
            'weather_summary'
        )
        load_instance = True
        ordered = True
