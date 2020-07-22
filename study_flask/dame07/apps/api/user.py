import random

from flask import Blueprint, jsonify, session
from flask_restful import Api, fields, marshal_with, Resource, reqparse, inputs
from werkzeug.security import generate_password_hash, check_password_hash

from apps.models.news_model import NewType
from apps.models.user_model import User
from apps.utils import send_duanxin

from exts import api, cache, db

user_bp = Blueprint('user', __name__, url_prefix='/api')


types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='type_name')
}

sms_parser = reqparse.RequestParser()
sms_parser.add_argument(
    'phone',
    type=inputs.regex(r'1[35789]\d{9}$'),
    help='请输入正确格式手机号',
    required=True,
    location=['form']
)

class SendMessageHandler(Resource):

    def post(self):
        args = sms_parser.parse_args()
        phone = args.get('phone')

        # 补充验证码手机号码是否注册，去数据库查询
        ret, code = send_duanxin(phone)

        # 验证是否发送成功
        if ret is not None:
            if ret['code'] == 200:
                # cache
                cache.set(phone, code, timeout=100)
                pass
        else:
            print('error: ')
            return jsonify(code=400, msg='短信发送失败')




# 定制输入
login_parser = sms_parser.copy()
login_parser.add_argument('code', type=inputs.regex(r'^\d{4}$'), help='验证码格式错误', required=True, locals='form')

# 定制输出
user_fields = {
    'id': fields.Integer,
    'username': fields.String()
}

# 登录注册
class LoginHandler(Resource):

    def post(self):
        args = login_parser.parse_args()
        phone = args.get('phone')
        code = args.get('code')

        cache_code = cache.get(phone)

        if cache_code and code == cache_code:
            # 验证码正确
            users = User.query.filter(User.phone == phone).first()
            if not users:
                # 注册处理
                user = User()
                user.phone = phone
                user.username = '用户' + phone
                db.session.add(user)
                db.commit()

            # 登录处理， 纪录登录状态
            cache.set(phone+'_', 1)
            return marshal_with(users, user_fields)
        else:
            return {'msg':'验证码错误', 'status': 4000}


# 发送验证码
class ForGetHandler(Resource):

    def get(self):

        code = ''
        s = 'qwertyuiopasdfghjklzxcvbnm'

        for i in range(4):
            ran = random.choice(s)
            code += ran

        session['code'] = code
        return {'code': code}


reset_parser = sms_parser.copy()
reset_parser.add_argument('code', type=inputs.regex(r'^[a-zA-Z0-9]{4}$'), help='验证码不正确')


# 重置密码
class ResetPwdHandler(Resource):

    def get(self):

        args = reset_parser.parse_args()
        phone= args.get('mobile')
        code = args.get('code')
        im_code = session.get('code')
        if code and im_code.low() == code.lower():
            # 判断手机号码
            user = User.query.filter(User.phone==phone).first()

            # 判断手机验证码
            ret, sms_code = send_duanxin(phone)

            if ret is not None:
                if ret['sms_code'] == 200:
                    cache.set(phone, sms_code, timeout=1800)
                    return jsonify(status=200, msg='短信发送成功')
            return jsonify(status=400, msg='短信发送失败')

        return jsonify(status=400, msg='验证码有误')

# 更新密码
update_parser = login_parser.copy()
update_parser.add_argument('password',type=inputs.regex(r'^\d{6}$'), help='请输入登录密码', locals='form')
update_parser.add_argument('repassword',type=inputs.regex(r'^\d{6}$'), help='请输入登录密码', locals='form')

# 密码登录
login_pwd_parser = sms_parser.copy()
login_pwd_parser = login_pwd_parser.add_argument('password', type=str, help='请输入密码', required=True, locals='form')


class PwdLoginHandler(Resource):

    def post(self):
        args = login_pwd_parser.args()
        phone = args.get('phone')
        password = args.get('password')

        # 判断用户是否存在
        user = User.query.filter(User.phone == phone).first()
        if user:
            if check_password_hash(user.password, password):
                cache.set(phone + '_', 1)
                return {'status': 200, 'msg': 'ok'}
        return {'status': 400, 'msg': '用户名或密码错误'}


    def put(self):
        agrs = update_parser.parse_args()
        code = agrs.get('code')
        phone = agrs.get('phone')
        cache_code = cache.get(phone)
        if cache_code and cache_code == code:
            user = User.query.filter(User.phone == phone).first()
            password = agrs.get('password')
            repassword = agrs.get('repassword')

            if password == repassword:
                user.password = generate_password_hash(password)
                db.session.commit()
                return {'status': 200, 'msg': 'ok'}
            return {'status': 200, 'msg': '两次密码不一致'}
        return {'status': 400, 'msg': '验证码有误'}




api.add_resource(LoginHandler, '/login')
api.add_resource(SendMessageHandler, '/sms')
api.add_resource(ForGetHandler, '/forget')
api.add_resource(ResetPwdHandler, '/reset')
api.add_resource(PwdLoginHandler, '/user_login')






