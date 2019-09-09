from flask_restful import Api, Resource

from app.main import create_app
from app.main.service.CatalogService import CatalogService

app = create_app()
api = Api(app)
data = CatalogService.get_catalog()


api.add_resource(CatalogService, '/')
# api.add_resource(CatalogService.get_by_rate(data, ['rate']), '/catalog/<int:rate>')
# api.add_resource(CatalogService.get_by_name(data, ['name']), '/catalog/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)


