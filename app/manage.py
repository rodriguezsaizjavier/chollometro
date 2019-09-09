from flask import Flask
from flask_restful import Resource, Api

from app.main.data.Data import chollo_conn, get_catalog
from app.main.utilities.Filters import filter_by_rate

app = Flask(__name__)
api = Api(app)
data = get_catalog(chollo_conn())


class Catalog(Resource):
    def get(self, rate):
        return filter_by_rate(data, rate)


api.add_resource(Catalog, '/catalog/<int:rate>')

if __name__ == '__main__':
    app.run(debug=True)
