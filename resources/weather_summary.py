from flask import request
from flask_restful import Resource
from models.weather_summary import WeatherSummaryModel
from schemas.weather_summary import WeatherSummarySchema

WEATHER_NOT_FOUND = 'Weather data not found.'
ERROR_FETCHING_WEATHER = 'An error occured while trying to fetch the'\
                         'weather data!'

weather_summary_schema = WeatherSummarySchema()


class WeatherSummary(Resource):
    def get(self):

        try:
            latitude = request.args.get('lat')
            longitude = request.args.get('lon')

            weather_summary = WeatherSummaryModel.find_by_longitude_and_latitude(
                longitude, latitude
            )
        except Exception as ex:
            return {'message': ERROR_FETCHING_WEATHER, 'Error': ex}, 500

        if weather_summary:
            return weather_summary_schema.dump(weather_summary), 200

        return {'message': WEATHER_NOT_FOUND}, 404
