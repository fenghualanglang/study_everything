

from flask import Blueprint
from flask_restful import Api, fields, marshal_with, Resource


from apps.models.news_model import NewType

from exts import api

news_bp = Blueprint('news', __name__, url_prefix='/api')


types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='type_name')
}



class NewsTypeHandler(Resource):

    @marshal_with(types_fields)
    def get(self):
        types = NewType.query.all()
        return types


api.add_resource(NewsTypeHandler, '/types')








