from ma import ma
from marshmallow import post_dump
from models.weather_summary import WeatherSummaryModel
from models.weather_data import WeatherDataModel


class WeatherSummarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeatherSummaryModel
        load_only = (
            'longitude',
            'latitude',
            'forecast_time',
            'weather_data'
        )
        include_fk = True
        load_instance = True
        ordered = True

    @post_dump(pass_original=True)
    def make_object(self, data, original_data, **kwargs):

        weather_summary_object = {
            'max': {
                'temperature': round(original_data.max_temperature, 2),
                'precipitation': round(original_data.max_precipitation, 2)
            },
            'min': {
                'temperature': round(original_data.min_temperature, 2),
                'precipitation': round(original_data.min_precipitation, 2)
            },
            'avg': {
                'temperature': round(original_data.avg_temperature, 2),
                'precipitation': round(original_data.avg_precipitation, 2)
            }
        }

        return weather_summary_object
