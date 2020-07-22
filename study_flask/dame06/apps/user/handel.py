
from flask import Blueprint
from flask_restful import Resource, marshal_with, fields, reqparse, inputs
from werkzeug.datastructures import FileStorage

from apps.user.model import User
from exts import api

handler_bp = Blueprint('user', __name__, url_prefix='/api')

# 返回数据序列化
user_fields = {
    'id': fields.Integer,
    'username':fields.String,
    # 自定义字段与后端映射，前端看不到数据库字段
    # 'private_name': fields.String(attribute='username', default='zhangsan')
    'phone': fields.String,
    'create_time': fields.DateTime,
    'email': fields.String
}

# 参数解析验证
parser = reqparse.RequestParser(bundle_errors=True)  # bundle_errors=True 默认为false
# type=类型, required=是否必传, help='提示语', location=['form'] post请求
parser.add_argument('username', type=str, required=True, help='请输入用户名', location=['form'])
parser.add_argument('phone', type=inputs.regex(r'^1[123456789]\d{9}$'), location=['form', 'args'])
parser.add_argument('email')
parser.add_argument('icon', type=FileStorage, location=['files'])

class UserResource(Resource):

    @marshal_with(user_fields)
    def get(self):

        users = User.query.all()

        return users
        pass

    def post(self):
        args = parser.parse_args()
        usrname = args.get('username')
        pass

class UserSimpleResource(Resource):

    @marshal_with(user_fields)
    def get(self, uid):
        users = User.query.get(uid)
        return users
        pass

    def post(self, uid):
        pass

# http://127.0.0.1:5000/user
api.add_resource(UserResource, '/user2')
# http://127.0.0.1:5000/user/1
api.add_resource(UserSimpleResource, '/user2/<int:uid>')



























