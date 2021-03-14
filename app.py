from os import environ

from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from ma import ma
from db import db
from load_data import load_csv_data
from resources.weather_data import WeatherData
from resources.weather_summary import WeatherSummary

import logging

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URL", "sqlite:///test.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)

@app.route('/')
def home():
    return 'Weather API App'

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(error):
    return jsonify(error.messages), 400


api.add_resource(WeatherData, "/weather/data")
api.add_resource(WeatherSummary, "/weather/summarize")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    load_csv_data(app.config["SQLALCHEMY_DATABASE_URI"])

    app.run(port=5000, debug=True)
