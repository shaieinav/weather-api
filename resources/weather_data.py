from flask import request
from flask_restful import Resource
from models.weather_data import WeatherDataModel
from schemas.weather_data import WeatherDataSchema

WEATHER_NOT_FOUND = 'Weather data not found.'
ERROR_FETCHING_WEATHER = 'An error occured while trying to fetch the'\
                         'weather data!'

weather_data_schema = WeatherDataSchema(many=True)


class WeatherData(Resource):
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
            return weather_data_schema.dump(weather), 200

        return {'message': WEATHER_NOT_FOUND}, 404
