from flask_restful import Api, Resource
from app.main import create_app
from app.main.data.Data2 import create_json, get_raw_data
from app.main.utilities.Filters import filter_by_rate, filter_by_name, filter_by_not_expired
from app.main.utilities.Utilities import reloaded

app = create_app()
api = Api(app)

# filters = list(filter(lambda x: filter_by_rate(x, 1) and filter_by_name(x, 'Nintendo'), get_data()))
# filters = list(filter(lambda x: filter_by_not_expired(x), get_data()))

data = create_json(get_raw_data(11))


class CatalogService(Resource):

    @staticmethod
    def get():
        return reloaded(data)


api.add_resource(CatalogService, '/catalog')
# api.add_resource(CatalogService.get_by_rate(data, ['rate']), '/catalog/<int:rate>')
# api.add_resource(CatalogService.get_by_name(data, ['name']), '/catalog/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)
