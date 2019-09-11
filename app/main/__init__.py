from flask import Flask
from app.main.data.Data import get_catalog
from app.main.data.Data2 import get_data

app = Flask(__name__)

data = get_data()


def get_catalog():
    return data


def create_app():
    return app
