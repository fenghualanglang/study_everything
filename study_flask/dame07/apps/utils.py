import random

from flask import request, abort, g

from apps.models.user_model import User
from apps.sms_send import SecretPair, SmsSendAPIDemo
from exts import cache


def send_duanxin(phone):

    SECRET_ID = '' # 产品id， 产品标识
    SECRET_KEY = ''  # 产品私有密钥，服务端生成签名信息
    BUSINESS_ID = ''  # 业务id， 易盾根据业务特点

    secret_pair = SecretPair(SECRET_ID, SECRET_KEY)
    api = SmsSendAPIDemo(BUSINESS_ID, secret_pair)

    # 产生验证码
    code = ''
    for i in range(4):
        ran = random.randint(0, 9)
        code += str(ran)

    params = {
        "mobile": phone,
        'templateId': '123456',
        "paramType": 'json',
        'params': {'code': code}
    }

    ret = api.send(params)

    return ret, code


def check_user():
    auth = request.headers.get('Authorization')
    if not auth:
        abort(401, msg='请登录')
    phone = cache.get(auth)
    if not phone:
        abort(401, msg='无效令牌')
    user = User.query.filter(User.phone == phone).first()
    if not user:
        abort(401, msg='请注册')
    g.user = User


# 登录验证
def login_required(func):
    def wrapper(*args, **kwargs):
        # 从缓存中获取登录信息
        check_user()
        return func(*args, **kwargs)
    return wrapper




























