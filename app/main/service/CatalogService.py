from app.main.data.Data import get_catalog
from app.main.utilities.Filters import filter_by_rate
from flask_restful import Resource


class CatalogService(Resource):

    @staticmethod
    def get_catalog():
        return get_catalog()

    # @staticmethod
    # def get_by_rate(data, rate):
    #     return filter_by_rate(data, rate)
    #
    # @staticmethod
    # def get_by_name(data, name):
    #     return filter_by_rate(data, name)
