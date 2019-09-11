from flask import Flask
from app.main.data.Data import get_catalog

app = Flask(__name__)

data = get_catalog()


def get_catalog():
    return data


def create_app():
    return app
