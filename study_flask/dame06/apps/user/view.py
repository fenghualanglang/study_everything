import json
from flask import Blueprint, request
from flask_restful import Resource

from apps.user.model import User
from exts import api

user_bp = Blueprint('user', __name__, url_prefix='/api')

class UserResource(Resource):

    def get(self):
        users = User.query.all()
        return users

    def post(self):

        req1 = request.get_json()
        req2 = request.json
        print('1', req1)
        print('2', req2)
        tt = json.loads(json.dumps(req1))
        print(tt)
        return {"code":200, "data":json.loads(json.dumps(req1)), "msg": "ok"}


api.add_resource(UserResource, '/user')



























