# Weather API

## Description

This project is a Python weather data API to find data about temperatures and precipitations given latitude and longitude parameters.

The project was built using Flask, Flask-RESTful, Marshmallow, and SQLAlchemy.

The Flask application is deployed with uWSGI and NGINX on DigitalOcean with PostgreSQL as DB.

## Usage

You can reach the application by following this link and try it yoursel:

[Weather API App](https://weather-api.app/weather/data?lat=-90&lon=-180)

The /weather/data route will show all the weather data exist for the given longitude and latitude.

The /weather/summarize route will show the weather statistics that  exist for the given longitude and latitude.

Changing the longitude and latitude parameters will give data for that location.
Valid parameters are -180 <= lon < 180, and -90 <= lat < 90, with 0.5 increments.

## Prerequisites

Python 3.8+

Virtualenv

## Installation

Clone the repository

```sh
git clone https://github.com/shaieinav/weather-api.git
```

cd to the repo directory

```sh
cd weather-api
```

Create a virtual environment

```sh
virtualenv venv
source venv/bin/activate
```

Install all the necessary dependencies

```sh
pip install -r requirements
```

Start the application
```sh
python app.py
```
