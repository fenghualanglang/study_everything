
from flask import Blueprint
from flask_restful import Resource, marshal_with, fields

from apps.user.model import User
from exts import api

user_bp = Blueprint('user', __name__, url_prefix='/api')

user_fields = {
    'id': fields.Integer,
    'username':fields.String,
    'create_time': fields.DateTime,
    'email': fields.String
}

class UserResource(Resource):

    @marshal_with(user_fields)
    def get(self):

        users = User.query.all()

        return users
        pass

    def post(self):
        pass



api.add_resource(UserResource, '/user')