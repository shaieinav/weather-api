from app import app
from db import db
from ma import ma
from load_data import load_csv_data

db.init_app(app)
ma.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


load_csv_data(app.config['SQLALCHEMY_DATABASE_URI'])
