from flask import request
from flask_restful import Resource
from models.weather_data import WeatherDataModel
from schemas.weather_summary import WeatherSummarySchema

WEATHER_NOT_FOUND = 'Weather data not found.'
ERROR_FETCHING_WEATHER = 'An error occured while trying to fetch the'\
                         'weather data!'

weather_summary_schema = WeatherSummarySchema(many=True)


class WeatherSummary(Resource):
    def get(self):

        try:
            latitude = request.args.get('lat')
            longitude = request.args.get('lon')

            weather = WeatherDataModel.find_by_longitude_and_latitude(
                longitude, latitude
            )
        except Exception as ex:
            return {'message': ERROR_FETCHING_WEATHER, 'Error': ex}, 500

        if weather:

            num_of_data_points = total_temperature = total_precipitation = 0
            minTemperature = maxTemperature = avgTemperature = None
            minPrecipitation = maxPrecipitation = avgPrecipitation = None

            for weather_data_point in weather:

                num_of_data_points += 1
                total_temperature += weather_data_point.temperature
                total_precipitation += weather_data_point.precipitation

                if (
                    minTemperature is None
                    or weather_data_point.temperature < minTemperature
                ):
                    minTemperature = weather_data_point.temperature
                if (
                    maxTemperature is None
                    or weather_data_point.temperature > maxTemperature
                ):
                    maxTemperature = weather_data_point.temperature
                if (
                    minPrecipitation is None
                    or weather_data_point.precipitation < minPrecipitation
                ):
                    minPrecipitation = weather_data_point.precipitation
                if (
                    maxPrecipitation is None
                    or weather_data_point.precipitation > maxPrecipitation
                ):
                    maxPrecipitation = weather_data_point.precipitation

            avgTemperature = round(total_temperature / num_of_data_points, 2)
            avgPrecipitation = round(total_precipitation / num_of_data_points, 2)

            weather_summary_obj = {
                "max": {
                    "Temperature": maxTemperature,
                    "Precipitation": maxPrecipitation,
                },
                "min": {
                    "Temperature": minTemperature,
                    "Precipitation": minPrecipitation,
                },
                "avg": {
                    "Temperature": avgTemperature,
                    "Precipitation": avgPrecipitation,
                },
            }

            return weather_summary_obj, 200

        return {'message': WEATHER_NOT_FOUND}, 404
