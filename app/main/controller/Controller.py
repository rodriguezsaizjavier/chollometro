from flask_restful import Api, Resource
from app.main import create_app
from app.main.data.Data2 import get_data

app = create_app()
api = Api(app)


class CatalogService(Resource):

    @staticmethod
    def get():
        return get_data()


api.add_resource(CatalogService, '/catalog')
# api.add_resource(CatalogService.get_by_rate(data, ['rate']), '/catalog/<int:rate>')
# api.add_resource(CatalogService.get_by_name(data, ['name']), '/catalog/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)
